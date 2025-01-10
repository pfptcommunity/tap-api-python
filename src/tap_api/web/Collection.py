"""
This code was tested against Python 3.9
 
Author: Ludvik Jerabek
Package: et_api
License: MIT
"""
from typing import List, TypeVar

from requests import Response

T = TypeVar('T')


class Collection(List[T]):
    __response: Response

    def __init__(self, response: Response):
        super().__init__(response.json())
        self.__response = response

    def get_status(self) -> int:
        return self.__response.status_code

    def get_reason(self) -> str:
        return self.__response.reason

    def get_response(self) -> Response:
        return self.__response
