"""
This code was tested against Python 3.9

Author: Ludvik Jerabek
Package: et_api
License: MIT
"""
from __future__ import annotations

from typing import List, TypeVar
from requests import Response
from requests.structures import CaseInsensitiveDict

T = TypeVar('T')


class Collection(List[T]):
    """
    A specialized list that wraps an HTTP response, providing access to both
    the JSON data (as a list) and the original response object.

    Methods:
        get_status() -> int:
            Returns the HTTP status code of the response.
        get_reason() -> str:
            Returns the HTTP reason phrase of the response.
        get_response() -> Response:
            Returns the original HTTP response object.
        get_headers() -> dict:
            Returns the HTTP headers from the response.
    """

    def __init__(self, response: Response):
        """
        Initializes the Collection with JSON data from an HTTP response.

        Args:
            response (Response): The HTTP response object.

        Raises:
            ValueError: If the response body is not valid JSON.
        """
        try:
            super().__init__(response.json())
            self.__response = response
        except ValueError as e:
            raise ValueError("Response does not contain valid JSON data.") from e

    def get_status(self) -> int:
        """
        Returns the HTTP status code of the response.

        Returns:
            int: The HTTP status code.
        """
        return self.__response.status_code

    def get_reason(self) -> str:
        """
        Returns the HTTP reason phrase of the response.

        Returns:
            str: The HTTP reason phrase.
        """
        return self.__response.reason

    def get_response(self) -> Response:
        """
        Returns the original HTTP response object.

        Returns:
            Response: The HTTP response object.
        """
        return self.__response

    def get_headers(self) -> CaseInsensitiveDict[str]:
        """
        Returns the HTTP headers from the response.

        Returns:
            dict: The HTTP headers.
        """
        return self.__response.headers


TCollection = TypeVar('TCollection', bound=Collection)