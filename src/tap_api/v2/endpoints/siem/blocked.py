"""
Author: Ludvik Jerabek
Package: tap_api
License: MIT
"""
from typing import Optional

from tap_api.common.campaign.filters import TimeParameter, SinceSeconds, SinceTime, TimeInterval
from tap_api.common.siem.filters import ThreatType, ThreatStatus
from tap_api.v2.endpoints.siem.siem_data import SIEMData
from tap_api.web import Resource, FilterOptions


class Blocked(Resource):
    def __init__(self, parent, uri: str):
        super().__init__(parent, uri)

    def __call__(self, time: TimeParameter, threat_type: Optional[ThreatType] = None,
                 threat_status: Optional[ThreatStatus] = None) -> SIEMData:
        options = FilterOptions()
        options.add_option("format", "json")
        options.add_option("threatType", threat_type)
        options.add_option("threatStatus", threat_status)

        if isinstance(time, SinceSeconds):
            options.add_option("sinceSeconds", time)
        elif isinstance(time, SinceTime):
            options.add_option("sinceTime", time)
        elif isinstance(time, TimeInterval):
            options.add_option("interval", time)
        else:
            # Raise an error for unsupported types
            raise TypeError(
                f"Unsupported type for time parameter: {type(time).__name__}. "
                f"Expected one of: SinceSeconds, SinceTime, TimeInterval."
            )
        return SIEMData(self._session.get(self._uri, params=options.params))
