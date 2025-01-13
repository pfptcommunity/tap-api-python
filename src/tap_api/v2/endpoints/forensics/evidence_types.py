from __future__ import annotations

from typing import Dict, Type, List


class EvidenceType(Dict):
    """
    Base class for the 'what' field in Forensics API.
    """

    def __init__(self, data):
        super().__init__(data)
        print(self.__class__.__name__)


class AttachmentEvidenceType(EvidenceType):
    @property
    def sha256(self) -> str:
        return self.get("sha256", "")

    @property
    def blacklisted(self) -> bool:
        return self.get("blacklisted", False)

    @property
    def md5(self) -> str:
        return self.get("md5", "")

    @property
    def offset(self) -> int:
        return self.get("offset", 0)

    @property
    def rule(self) -> str:
        return self.get("rule", "")

    @property
    def size(self) -> int:
        return self.get("size", 0)


class BehaviorEvidenceType(EvidenceType):
    @property
    def rule(self) -> str:
        return self.get("rule", "")

    @property
    def note(self) -> str:
        return self.get("note", "")

    @property
    def malicious(self) -> bool:
        return self.get("malicious", False)


class CookieEvidenceType(EvidenceType):
    @property
    def action(self) -> str:
        return self.get("action", "")

    @property
    def domain(self) -> str:
        return self.get("domain", "")

    @property
    def key(self) -> str:
        return self.get("key", "")

    @property
    def value(self) -> str:
        return self.get("value", "")


class DNSEvidenceType(EvidenceType):
    @property
    def host(self) -> str:
        return self.get("host", "")

    @property
    def cnames(self) -> List[str]:
        return self.get("cnames", [])

    @property
    def ips(self) -> List[str]:
        return self.get("ips", [])

    @property
    def nameservers(self) -> List[str]:
        return self.get("nameservers", [])

    @property
    def nameservers_list(self) -> List[str]:
        return self.get("nameserversList", [])


class DropperEvidenceType(EvidenceType):
    @property
    def path(self) -> str:
        return self.get("path", "")

    @property
    def rule(self) -> str:
        return self.get("rule", "")

    @property
    def url(self) -> str:
        return self.get("url", "")


class FileEvidenceType(EvidenceType):
    @property
    def sha256(self) -> str:
        return self.get("sha256", "")

    @property
    def size(self) -> int:
        return self.get("size", 0)

    @property
    def path(self) -> str:
        return self.get("path", "")


class IDSEvidenceType(EvidenceType):
    @property
    def name(self) -> str:
        return self.get("name", "")

    @property
    def signature_id(self) -> int:
        return self.get("signatureId", 0)


class MutexEvidenceType(EvidenceType):
    def __init__(self, data: Dict):
        super().__init__(data)
        print("Doing MUTEX")

    @property
    def name(self) -> str:
        return self.get("name", "")

    @property
    def path(self) -> str:
        return self.get("path", "")


class NetworkEvidenceType(EvidenceType):
    @property
    def action(self) -> str:
        return self.get("action", "")

    @property
    def ip(self) -> str:
        return self.get("ip", "")

    @property
    def port(self) -> str:
        return self.get("port", "")

    @property
    def protocol_type(self) -> str:
        return self.get("type", "")


class ProcessEvidenceType(EvidenceType):
    @property
    def path(self) -> str:
        return self.get("path", "")

    @property
    def action(self) -> str:
        return self.get("action", "")


class RegistryEvidenceType(EvidenceType):
    @property
    def action(self) -> str:
        return self.get("action", "")

    @property
    def key(self) -> str:
        return self.get("key", "")

    @property
    def name(self) -> str:
        return self.get("name", "")

    @property
    def rule(self) -> str:
        return self.get("rule", "")

    @property
    def value(self) -> str:
        return self.get("value", "")


class RuleEvidenceType(EvidenceType):
    @property
    def rule(self) -> str:
        return self.get("rule", "")


class ScreenshotEvidenceType(EvidenceType):
    @property
    def url(self) -> str:
        return self.get("url", "")


class URLEvidenceType(EvidenceType):
    @property
    def url(self) -> str:
        return self.get("url", "")

    @property
    def blacklisted(self) -> bool:
        return self.get("blacklisted", False)

    @property
    def ip(self) -> str:
        return self.get("ip", "")

    @property
    def http_status(self) -> int:
        return self.get("httpStatus", 0)

    @property
    def md5(self) -> str:
        return self.get("md5", "")

    @property
    def offset(self) -> int:
        return self.get("offset", 0)

    @property
    def rule(self) -> str:
        return self.get("rule", "")

    @property
    def sha256(self) -> str:
        return self.get("sha256", "")

    @property
    def size(self) -> int:
        return self.get("size", 0)


def create_evidence_type(data: Dict, evidence_type: str) -> EvidenceType:
    subclass = _EVIDENCE_TYPE_REGISTRY.get(evidence_type, EvidenceType)
    return subclass(data)


# Registry for WhatInfo subclasses
_EVIDENCE_TYPE_REGISTRY: Dict[str, Type[EvidenceType]] = {
    "attachment": AttachmentEvidenceType,
    "behavior": BehaviorEvidenceType,
    "cookie": CookieEvidenceType,
    "dns": DNSEvidenceType,
    "dropper": DropperEvidenceType,
    "file": FileEvidenceType,
    "ids": IDSEvidenceType,
    "mutex": MutexEvidenceType,
    "network": NetworkEvidenceType,
    "process": ProcessEvidenceType,
    "registry": RegistryEvidenceType,
    "rule": RuleEvidenceType,
    "screenshot": ScreenshotEvidenceType,
    "url": URLEvidenceType,
}
