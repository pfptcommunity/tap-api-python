"""
This code was tested against Python 3.9

Author: Ludvik Jerabek
Package: tap_api
License: MIT
"""
from typing import List, Callable, overload

from requests import Response, PreparedRequest

from tap_api.v2.endpoints.people.vap_info import VapInfo
from tap_api.v2.filters.vap_options import VapOptions
from tap_api.web.resource import Resource


class Vap(Resource):
    def __init__(self, parent, uri: str):
        super().__init__(parent, uri)

    def __call__(self, options: VapOptions) -> VapInfo:
        return VapInfo(self.session.get(self.uri, params=options.params))
