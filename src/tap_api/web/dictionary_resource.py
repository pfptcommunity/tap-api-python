"""
This code was tested against Python 3.9

Author: Ludvik Jerabek
Package: tap_api
License: MIT
"""
from __future__ import annotations

from typing import TypeVar, Type, Generic

from .dictionary import Dictionary
from .resource import Resource

T = TypeVar('T', bound=Dictionary)


class DictionaryResource(Generic[T], Resource):
    __dict_type: Type[T]

    def __init__(self, parent, uri: str, dict_type: Type[T] = Dictionary):
        super().__init__(parent, uri)
        self.__dict_type = dict_type

    def __call__(self) -> T:
        return self.__dict_type(self.session.get(self.uri))
