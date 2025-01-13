"""
This code was tested against Python 3.9

Author: Ludvik Jerabek
Package: tap_api
License: MIT
"""
from datetime import datetime
from typing import Dict, List

from requests import Response

from tap_api.web import Dictionary


class Actor(Dict):
    @property
    def id(self) -> str:
        return self.get("id", "")

    @property
    def name(self) -> str:
        return self.get("name", "")


class Family(Dict):
    @property
    def id(self) -> str:
        return self.get("id", "")

    @property
    def name(self) -> str:
        return self.get("name", "")


class Malware(Dict):
    @property
    def id(self) -> str:
        return self.get("id", "")

    @property
    def name(self) -> str:
        return self.get("name", "")


class Technique(Dict):
    @property
    def id(self) -> str:
        return self.get("id", "")

    @property
    def name(self) -> str:
        return self.get("name", "")


class Brand(Dict):
    @property
    def id(self) -> str:
        return self.get("id", "")

    @property
    def name(self) -> str:
        return self.get("name", "")


class ThreatInfo(Dictionary):
    def __init__(self, response: Response):
        super().__init__(response)

    @property
    def id(self) -> str:
        return self.get('id', "")

    @property
    def identified_at(self) -> datetime:
        return self.get('identifiedAt', None)

    @property
    def name(self) -> str:
        return self.get('name', "")

    @property
    def type(self) -> str:
        return self.get('type', "")

    @property
    def category(self) -> str:
        return self.get('category', "")

    @property
    def status(self) -> str:
        return self.get('status', "")

    @property
    def detection_type(self) -> str:
        return self.get('detectionType', "")

    @property
    def severity(self) -> int:
        return self.get('severity', 0)

    @property
    def attack_spread(self) -> int:
        return self.get('attackSpread', 0)

    @property
    def notable(self) -> bool:
        return self.get('notable', False)

    @property
    def verticals(self) -> bool:
        return self.get('verticals', False)

    @property
    def geographies(self) -> bool:
        return self.get('geographies', False)

    @property
    def actors(self) -> List[Actor]:
        return [Actor(actor) for actor in self.get("actors", [])]

    @property
    def families(self) -> List[Family]:
        return [Family(family) for family in self.get("families", [])]

    @property
    def malware(self) -> List[Malware]:
        return [Malware(m) for m in self.get("malware", [])]

    @property
    def techniques(self) -> List[Technique]:
        return [Technique(t) for t in self.get("techniques", [])]

    @property
    def brands(self) -> List[Brand]:
        return [Brand(b) for b in self.get("brands", [])]
