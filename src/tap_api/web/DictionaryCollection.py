"""
This code was tested against Python 3.9

Author: Ludvik Jerabek
Package: tap_api
License: MIT
"""
from typing import TypeVar, Type, List, Callable, Dict

from requests import Response

D = TypeVar('D', bound='Dict')


class DictionaryCollection(List[D]):
    __dictionary_type: Type[D]
    __response: Response

    def __init__(self, response: Response, transform: Callable[[Response], List] = lambda r: r.json(),
                 dictionary_type: Type[D] = Dict):
        super().__init__(transform(response))
        self.__response = response
        self.__dictionary_type = dictionary_type
        for idx, x in enumerate(self):
            self[idx] = self.__dictionary_type(x)

    def get_status(self) -> int:
        return self.__response.status_code

    def get_reason(self) -> str:
        return self.__response.reason

    def get_response(self) -> Response:
        return self.__response
