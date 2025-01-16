"""
Author: Ludvik Jerabek
Package: tap_api
License: MIT
"""
from tap_api.common.campaign.filters import TimeParameter, SinceSeconds, SinceTime, StartEndInterval
from tap_api.v2.endpoints.siem.siem_data import SIEMData
from tap_api.web import Resource, FilterOptions


class Blocked(Resource):
    def __init__(self, parent, uri: str):
        super().__init__(parent, uri)

    def __call__(self, time: TimeParameter) -> SIEMData:
        options = FilterOptions()
        options.add_option("format", "json")
        if isinstance(time, SinceSeconds):
            options.add_option("sinceSeconds", time)
        elif isinstance(time, SinceTime):
            options.add_option("sinceTime", time)
        elif isinstance(time, StartEndInterval):
            options.add_option("sinceTime", time)
        else:
            # Raise an error for unsupported types
            raise TypeError(
                f"Unsupported type for time parameter: {type(time).__name__}. "
                f"Expected one of: SinceSeconds, SinceTime, StartEndInterval."
            )
        return SIEMData(self.session.get(self.uri, params=options.params))

