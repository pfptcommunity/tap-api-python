"""
This code was tested against Python 3.9

Author: Ludvik Jerabek
Package: tap_api
License: MIT
"""
from __future__ import annotations

from typing import TypeVar, Type, Generic
from .collection import Collection, TCollection
from .resource import Resource

class CollectionResource(Generic[TCollection], Resource):
    """
    Represents a resource that maps to a collection-like object.

    Attributes:
        _collection_type (Type[TCollection]): The type of collection to use for resource data.
    """

    def __init__(self, parent: Resource, uri: str, collection_type: Type[TCollection] = Collection):
        """
        Initializes a new CollectionResource.

        Args:
            parent (Resource): The parent resource.
            uri (str): The name/URI segment for this resource.
            collection_type (Type[TCollection]): The collection type to use for resource data. Defaults to `Collection`.
        """
        super().__init__(parent, uri)
        self.__collection_type = collection_type

    def __call__(self) -> TCollection:
        """
        Fetches the resource data and returns it as an instance of the collection type.

        Returns:
            TCollection: An instance of the collection type containing the resource data.

        Raises:
            requests.exceptions.RequestException: If the HTTP request fails.
            ValueError: If the response data cannot be converted to the specified collection type.
        """
        try:
            return self.__collection_type(self.session.get(self.uri))
        except Exception as e:
            raise ValueError(f"Failed to fetch or parse resource data from {self.uri}: {e}")
