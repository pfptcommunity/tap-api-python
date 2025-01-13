from typing import Dict

from tap_api.v2.endpoints.people.identity import Identity
from tap_api.v2.endpoints.people.threat_statistics import ThreatStatistics


class User(Dict):
    @property
    def identity(self) -> Identity:
        return Identity(self.get("identity", {}))

    @property
    def threat_statistics(self) -> ThreatStatistics:
        return ThreatStatistics(self.get("threatStatistics", {}))
