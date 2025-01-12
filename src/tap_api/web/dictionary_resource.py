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

TDictionary = TypeVar('TDictionary', bound=Dictionary)


class DictionaryResource(Generic[TDictionary], Resource):
    """
    Represents a resource that maps to a dictionary-like object.

    Attributes:
        _dict_type (Type[TDictionary]): The type of dictionary to use for resource data.
    """

    def __init__(self, parent: Resource, uri: str, dict_type: Type[TDictionary] = Dictionary):
        """
        Initializes a new DictionaryResource.

        Args:
            parent (Resource): The parent resource.
            uri (str): The name/URI segment for this resource.
            dict_type (Type[TDictionary]): The dictionary type to use for resource data. Defaults to `Dictionary`.
        """
        super().__init__(parent, uri)
        self.__dict_type = dict_type

    def __call__(self) -> TDictionary:
        """
        Fetches the resource data and returns it as an instance of the dictionary type.

        Returns:
            TDictionary: An instance of the dictionary type containing the resource data.

        Raises:
            requests.exceptions.RequestException: If the HTTP request fails.
            ValueError: If the response data cannot be converted to the specified dictionary type.
        """
        try:
            return self.__dict_type(self.session.get(self.uri))
        except Exception as e:
            raise ValueError(f"Failed to fetch or parse resource data from {self.uri}: {e}")
