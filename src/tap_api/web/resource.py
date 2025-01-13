"""
This code was tested against Python 3.9

Author: Ludvik Jerabek
Package: tap_api
License: MIT
"""
from __future__ import annotations

from posixpath import join
from typing import Union, TypeVar

from requests import Session


class Resource:
    __session = Session()  # Shared session for all Resource instances
    """
    Represents a resource in a hierarchical structure with a URI.

    Attributes:
        __parent (Resource | None): The parent resource.
        __name (str): The name of the resource.
    """

    def __init__(self, parent: Union[Resource, None], uri: str):
        """
        Initializes a new Resource.

        Args:
            parent (Resource | None): The parent resource.
            uri (str): The name/URI segment for this resource.
        """
        self.__parent = parent
        self.__name = uri

    @property
    def name(self) -> str:
        """Gets the name of the resource."""
        return self.__name

    @property
    def uri(self) -> str:
        """
        Constructs the full URI for this resource by traversing its parent chain.

        Returns:
            str: The full URI.
        """
        visited = set()  # Track visited nodes to prevent infinite loops
        uri = self.__name
        parent = self.__parent

        while parent is not None:
            if id(parent) in visited:
                raise ValueError("Cyclic parent reference detected.")
            visited.add(id(parent))
            uri = join(parent.name, uri)
            parent = parent.__parent
        return uri

    @property
    def session(self) -> Session:
        """Gets the HTTP session associated with this resource."""
        return self.__session


TResource = TypeVar('TResource', bound=Resource)
