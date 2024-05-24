import datetime
import functools
import glob
import ipaddress
import os
import sys
import tempfile
from dataclasses import dataclass
from dataclasses import field
from enum import Enum
from typing import List

import humanize
import requests
import yaml
from loguru import logger

from cdnmon.util import bgpview
from cdnmon.util import db
from cdnmon.util.cidr import deduplicate_networks

logger.remove()
logger.add(sys.stderr, level="INFO")


class ETL:
    def extract(self):
        raise NotImplementedError

    def transform(self, data):
        raise NotImplementedError

    def load(self, data):
        raise NotImplementedError


class CIDR(ETL):
    def ipv4_prefixes(self) -> List[str]:
        return self.transform(self.extract())["ipv4_prefixes"]

    def ipv6_prefixes(self) -> List[str]:
        return self.transform(self.extract())["ipv6_prefixes"]

    @functools.lru_cache(maxsize=None)
    def http_get(self, url):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/107.0.0.0 Safari/537.36 "
        }
        response = requests.get(url, headers=headers)
        logger.info(
            f"{response.status_code} {response.reason} | GET {url}  ({humanize.naturalsize(len(response.content))} Bytes)"
        )
        return response


class BGPViewCIDR(CIDR):
    def __init__(self, query_term_list: List[str] = []):
        self.query_term_list = query_term_list
        self.bgpview_client = bgpview.BGPViewClient()

    def ipv4_prefixes(self) -> List[str]:
        ipv4_networks = []
        for query_term in self.query_term_list:
            data = self.bgpview_client.search(query_term)
            for item in data["data"]["ipv4_prefixes"]:
                ipv4_networks.append(str(ipaddress.IPv4Network(item["prefix"], strict=False)))
        return deduplicate_networks(ipv4_networks, filter_version=4)

    def ipv6_prefixes(self) -> List[str]:
        ipv6_networks = []
        for query_term in self.query_term_list:
            data = self.bgpview_client.search(query_term)
            for item in data["data"]["ipv6_prefixes"]:
                ipv6_networks.append(str(ipaddress.IPv6Network(item["prefix"], strict=False)))
        return deduplicate_networks(ipv6_networks, filter_version=6)


@dataclass
class CNAMEPattern:
    suffix: str = field(default_factory=str)
    pattern: str = field(default_factory=str)
    source: str = field(default_factory=str)

    def __str__(self) -> str:
        return self.suffix

    def __repr__(self) -> str:
        return self.suffix

    def marshal(self) -> dict:
        return {
            "suffix": self.suffix,
            "pattern": self.pattern,
            "source": self.source,
            "subscribers": self.subscribers(),
        }

    def subscribers(self) -> List[str]:
        if not os.getenv("MONGODB_URI"):
            logger.warning("MONGODB_URI is not set")
            return []

        suffix = self.suffix if self.suffix.endswith(".") else self.suffix + "."
        pattern = f'^{suffix[::-1].replace(".", chr(92)+".")}'
        filter = {
            "task.dns.response.answers.cname_reverse": {"$regex": pattern},
        }
        collection = db.get_mongo_collection("kepler", "dns")
        domain_set = set()
        for item in collection.find(filter).limit(1):
            qname = item["task"]["qname"]
            logger.warning("{} | {}", qname, self.suffix)
            domain_set.add(qname)
        return list(domain_set)


class DomainOwnershipVerficationStatus(Enum):
    REQUIRED = "required"
    NOT_REQUIRED = "not_required"
    UNKNOWN = "unknown"

    def __str__(self) -> str:
        return self.value


@dataclass
class DomainOwnershipVerification:
    status: DomainOwnershipVerficationStatus = field(default=DomainOwnershipVerficationStatus.UNKNOWN)
    prefix: str = field(default_factory=str)
    pattern: str = field(default_factory=str)

    def __dict__(self) -> dict:
        result = {"status": str(self.status)}
        if self.status == DomainOwnershipVerficationStatus.REQUIRED:
            result["prefix"] = self.prefix
            result["pattern"] = self.pattern
        return result


@dataclass
class HTTPOwnershipVerification:
    status: DomainOwnershipVerficationStatus = field(default=DomainOwnershipVerficationStatus.UNKNOWN)
    path: str = field(default_factory=str)
    pattern: str = field(default_factory=str)

    def __dict__(self) -> dict:
        result = {"status": str(self.status)}
        if self.status == DomainOwnershipVerficationStatus.REQUIRED:
            result["path"] = self.path
            result["pattern"] = self.pattern
        return result


@dataclass
class OwnershipVerification:
    txt: DomainOwnershipVerification = field(default_factory=DomainOwnershipVerification)
    http: HTTPOwnershipVerification = field(default_factory=HTTPOwnershipVerification)

    def __dict__(self) -> dict:
        result = {}
        if self.txt.status != DomainOwnershipVerficationStatus.UNKNOWN:
            result["txt"] = self.txt.__dict__()
        if self.http.status != DomainOwnershipVerficationStatus.UNKNOWN:
            result["http"] = self.http.__dict__()
        return result


@dataclass
class CommonCDN:
    name: str = field(default_factory=str)
    asn_patterns: list[str] = field(default_factory=list)
    cname_suffixes: list[CNAMEPattern] = field(default_factory=list)
    cidr: CIDR = field(default_factory=CIDR)
    frontend_ownership_verification: OwnershipVerification = field(default_factory=OwnershipVerification)
    backend_ownership_verification: OwnershipVerification = field(default_factory=OwnershipVerification)

    def ipv4_prefixes(self) -> List[str]:
        return self.cidr.ipv4_prefixes()

    def ipv6_prefixes(self) -> List[str]:
        return self.cidr.ipv6_prefixes()

    def subscribers(self) -> List[str]:
        results = set()
        for cname_suffix in self.cname_suffixes:
            for subscriber in cname_suffix.subscribers():
                results.add(subscriber)
        return list(results)

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name

    def dump(self) -> bool:
        path = os.path.join(
            os.path.dirname(
                os.path.dirname(
                    os.path.dirname(
                        os.path.dirname(__file__),
                    ),
                ),
            ),
            "assets",
            "cdn",
            f"{self.name}.yaml",
        )

        old_content = ""
        if os.path.exists(path):
            with open(path, mode="r", encoding="utf-8") as f:
                old_content = f.read()

        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", delete=False) as f:
            temporary_filename = f.name
            yaml.dump(
                {
                    "name": self.name,
                    "asn_patterns": self.asn_patterns,
                    "cname_suffixes": [i.marshal() for i in self.cname_suffixes],
                    "ipv4_prefixes": self.ipv4_prefixes(),
                    "ipv6_prefixes": self.ipv6_prefixes(),
                    "frontend_ownership_verification": self.frontend_ownership_verification.__dict__(),
                    "backend_ownership_verification": self.backend_ownership_verification.__dict__(),
                    "updated_at": datetime.datetime.now().isoformat(),
                },
                f,
            )

        with open(temporary_filename, mode="r", encoding="utf-8") as f:
            new_content = f.read()

        old_lines = [line for line in old_content.splitlines() if not line.startswith("updated_at:")]
        new_lines = [line for line in new_content.splitlines() if not line.startswith("updated_at:")]

        if old_lines != new_lines:
            # move temporary file to the original file
            os.replace(temporary_filename, path)
            return True
        else:
            # remove temporary file
            os.remove(temporary_filename)
            return False


__all__ = []
for path in glob.glob(f"{os.path.dirname(__file__)}/*.py"):
    name, _ = os.path.splitext(os.path.basename(path))
    if name != "__init__":
        __all__.append(name)
