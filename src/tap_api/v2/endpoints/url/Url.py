"""
This code was tested against Python 3.9
 
Author: Ludvik Jerabek
Package: tap_api
License: MIT
"""
from tap_api.v2.endpoints.url.Decode import Decode
from tap_api.web import Resource


class Url(Resource):
    __decode = Decode

    def __init__(self, parent, uri: str):
        super().__init__(parent, uri)
        self.__decode = Decode(self, 'decode')

    @property
    def decode(self) -> Decode:
        return self.__decode
