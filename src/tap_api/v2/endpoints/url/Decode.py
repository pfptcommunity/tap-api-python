"""
This code was tested against Python 3.9

Author: Ludvik Jerabek
Package: tap_api
License: MIT
"""
from typing import List, Callable

from requests import Response

from tap_api.v2.endpoints.url.UrlInfo import UrlInfo
from tap_api.web.DictionaryCollection import DictionaryCollection
from tap_api.web.Resource import Resource


class Decode(Resource):
    def __init__(self, parent, uri: str):
        super().__init__(parent, uri)

    def __call__(self, urls: List[str]) -> DictionaryCollection[UrlInfo]:
        transform: Callable[[Response], list] = lambda r: r.json().get('urls', [])
        return DictionaryCollection[UrlInfo](self.session.post(self.uri, json={"urls": urls}), transform, UrlInfo)
