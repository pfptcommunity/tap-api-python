"""
This code was tested against Python 3.9

Author: Ludvik Jerabek
Package: tap_api
License: MIT
"""
from typing import TypeVar, Type, List, Callable, Dict
from requests import Response
from requests.structures import CaseInsensitiveDict

DictType = TypeVar('DictType', bound=Dict)


class DictionaryCollection(List[DictType]):
    """
    A specialized collection of dictionaries that wraps an HTTP response, allowing customization of
    transformation and dictionary type.

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

    def __init__(self, response: Response, transform: Callable[[Response], List] = lambda r: r.json(),
                 dictionary_type: Type[DictType] = Dict):
        """
        Initializes the DictionaryCollection.

        Args:
            response (Response): The HTTP response object.
            transform (Callable[[Response], List]): A function to transform the response into a list. Defaults to JSON decoding.
            dictionary_type (Type[D]): The type of dictionary to use for collection items. Defaults to `Dict`.

        Raises:
            ValueError: If the transformation does not produce a list.
            TypeError: If an item in the list cannot be converted to the specified dictionary type.
        """
        try:
            transformed_data = transform(response)
            if not isinstance(transformed_data, list):
                raise ValueError("Transform function must return a list.")
            super().__init__(transformed_data)
            self.__response = response
            self.__dictionary_type = dictionary_type
            for idx, x in enumerate(self):
                self[idx] = self.__dictionary_type(x)
        except Exception as e:
            raise ValueError(f"Failed to initialize DictionaryCollection: {e}")

    def get_status(self) -> int:
        """Returns the HTTP status code of the response."""
        return self.__response.status_code

    def get_reason(self) -> str:
        """Returns the HTTP reason phrase of the response."""
        return self.__response.reason

    def get_response(self) -> Response:
        """Returns the original HTTP response object."""
        return self.__response

    def get_headers(self) -> CaseInsensitiveDict[str]:
        """Returns the HTTP headers from the response."""
        return self.__response.headers
