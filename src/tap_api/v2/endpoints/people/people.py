"""
This code was tested against Python 3.9
 
Author: Ludvik Jerabek
Package: tap_api
License: MIT
"""

from tap_api.web import Resource
from .vap import Vap

class People(Resource):
    def __init__(self, parent, uri: str):
        super().__init__(parent, uri)

    @property
    def vap(self) -> Vap:
        return Vap(self,"vap")