"""
Author: Ludvik Jerabek
Package: tap_api
License: MIT
"""
from tap_api.v2.endpoints.siem.siem_data import SIEMData
from tap_api.web import Resource


class Issues(Resource):
    def __init__(self, parent, uri: str):
        super().__init__(parent, uri)

    def __call__(self) -> SIEMData:
        return SIEMData(self.session.get(self.uri))
