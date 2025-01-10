"""
This code was tested against Python 3.9

Author: Ludvik Jerabek
Package: et_api
License: MIT
"""
from __future__ import annotations

from typing import TypeVar, Type, Generic

from .Resource import Resource

TResource = TypeVar('TResource', bound='Resource')


class Resources(Generic[TResource], Resource):
    __res: Type[TResource]

    def __init__(self, parent, uri: str, res: Type[TResource]):
        super().__init__(parent, uri)
        self.__res = res

    def __getitem__(self, domain: str) -> TResource:
        return self.__res(self, domain.casefold().strip())
