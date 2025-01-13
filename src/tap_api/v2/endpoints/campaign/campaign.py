"""
Author: Ludvik Jerabek
Package: tap_api
License: MIT
"""
from tap_api.web import Resource
from .ids import Ids

class Campaign(Resource):
    def __init__(self, parent, uri: str):
        super().__init__(parent, uri)

    @property
    def ids(self) -> Ids:
        return Ids(self, "ids")