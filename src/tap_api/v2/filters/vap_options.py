from tap_api.common.people.filters import TimeWindow
from tap_api.web.filter_options import FilterOptions, TFilterOptions

class VapOptions(FilterOptions):
    __WINDOW = "window"

    def __init__(self) -> None:
        super().__init__()

    def set_window(self, window: TimeWindow) -> TFilterOptions:
        self._options[self.__WINDOW] = window
        return self

    def get_window(self) -> TimeWindow:
        return self._options[self.__WINDOW]
