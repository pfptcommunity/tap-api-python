"""
Author: Ludvik Jerabek
Package: tap_api
License: MIT
"""
from .summary import Summary
from tap_api.web import Resource, Resources


class Threat(Resource):
    __summary: Resources[Summary]

    def __init__(self, parent, uri: str):
        super().__init__(parent, uri)
        self.__summary = Resources[Summary](self, "summary", Summary)

    @property
    def summary(self) -> Resources[Summary]:
        return self.__summary
