from __future__ import annotations

from typing import Dict, Type, Optional

class EvidenceType(Dict):
    """
    Base class for the 'what' field in Forensics API.
    """
    def __init__(self, data):
        super().__init__(data)
        print(self.__class__.__name__)


class RuleEvidenceType(EvidenceType):
    @property
    def rule(self) -> str:
        return self.get("rule", "")

class AttachmentEvidenceType(EvidenceType):
    @property
    def sha256(self) -> str:
        return self.get("sha256", "")

    @property
    def blacklisted(self) -> int:
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

class URLEvidenceType(EvidenceType):
    @property
    def url(self) -> str:
        return self.get("url", "")

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


class ActionEvidenceType(EvidenceType):
    @property
    def action(self) -> str:
        return self.get("action", "")

    @property
    def ip(self) -> str:
        return self.get("ip", "")

    @property
    def port(self) -> int:
        return self.get("port", 0)


def create_evidence_type(data: Dict, evidence_type: str) -> EvidenceType:
    subclass = _WHAT_INFO_REGISTRY.get(evidence_type, EvidenceType)
    return subclass(data)

# Registry for WhatInfo subclasses
_WHAT_INFO_REGISTRY: Dict[str, Type[EvidenceType]] = {
    "attachment": AttachmentEvidenceType,
    "behavior": BehaviorEvidenceType,
    "cookie": CookieEvidenceType,
    "rule": RuleEvidenceType,
    "file": FileEvidenceType,
    "url": URLEvidenceType,
    "mutex": MutexEvidenceType,
    "action": ActionEvidenceType,
}
