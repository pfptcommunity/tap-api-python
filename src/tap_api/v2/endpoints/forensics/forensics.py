"""
This code was tested against Python 3.9
 
Author: Ludvik Jerabek
Package: tap_api
License: MIT
"""
from requests import Response

from tap_api.v2.endpoints.forensics.aggregate import AggregateForensics
from tap_api.web import Resource, Dictionary, FilterOptions


class Forensics(Resource):
    def __init__(self, parent, uri: str):
        super().__init__(parent, uri)

    def campaign(self, campaign_id: str) -> Dictionary:
        options = FilterOptions()
        options.add_option("campaign",campaign_id)
        return Dictionary(self.session.get(self.uri,params=options.params))

    def threat(self, threat_id: str, campaign_forensics: bool = False) -> AggregateForensics:
        options = FilterOptions()
        options.add_option("threatId", threat_id)
        options.add_option("includecampaignforensics",campaign_forensics)
        return AggregateForensics(self.session.get(self.uri, params=options.params))