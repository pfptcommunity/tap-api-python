from typing import Optional
from tap_api.common.people.filters import TimeWindow
from tap_api.web.filter_options import FilterOptions, TFilterOptions


class VapOptions(FilterOptions):
    """
    Provides filtering options for Very Attacked People (VAP) in the People API.
    """
    __WINDOW = "window"
    __PAGE = "page"
    __SIZE = "size"

    def __init__(self, window: TimeWindow = TimeWindow.DAYS_30, page: Optional[int] = None, size: Optional[int] = None,) -> None:
        """
        Initializes the VapOptions instance with default options.
        """
        super().__init__()
        self.set_window(window)

    # Time Window
    def set_window(self, window: TimeWindow) -> TFilterOptions:
        """
        Sets the time window filter.

        Args:
            window (TimeWindow): The time window object to set.

        Returns:
            TFilterOptions: The current instance of VapOptions.
        """
        self._options[self.__WINDOW] = window
        return self

    def get_window(self) -> Optional[TimeWindow]:
        """
        Retrieves the time window filter.

        Returns:
            Optional[TimeWindow]: The currently set time window, or None if not set.
        """
        return self._options.get(self.__WINDOW)

    # Pagination
    def set_page(self, page: int) -> TFilterOptions:
        """
        Sets the page number for the query.

        Args:
            page (int): The page number (must be 1 or greater).

        Returns:
            TFilterOptions: The current instance of VapOptions.
        """
        if page < 1:
            raise ValueError("Page number must be 1 or greater.")
        self._options[self.__PAGE] = page
        return self

    def get_page(self) -> Optional[int]:
        """
        Retrieves the page number.

        Returns:
            Optional[int]: The page number, or None if not set.
        """
        return self._options.get(self.__PAGE)

    def set_size(self, size: int) -> TFilterOptions:
        """
        Sets the page size for the query.

        Args:
            size (int): The number of results per page (must be positive).

        Returns:
            TFilterOptions: The current instance of VapOptions.
        """
        if size < 1:
            raise ValueError("Page size must be 1 or greater.")
        self._options[self.__SIZE] = size
        return self

    def get_size(self) -> Optional[int]:
        """
        Retrieves the page size.

        Returns:
            Optional[int]: The page size, or None if not set.
        """
        return self._options.get(self.__SIZE)
