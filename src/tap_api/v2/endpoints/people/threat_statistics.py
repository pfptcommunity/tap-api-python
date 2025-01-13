from typing import Dict, List

from tap_api.v2.endpoints.people.threat_family import ThreatFamily


class ThreatStatistics(Dict):
    @property
    def attack_index(self) -> int:
        return self.get("attackIndex", 0)

    @property
    def families(self) -> List[ThreatFamily]:
        return [ThreatFamily(family) for family in self.get("families", [])]