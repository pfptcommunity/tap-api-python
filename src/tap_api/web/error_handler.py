"""
This code was tested against Python 3.9

Author: Ludvik Jerabek
Package: tap_api
License: MIT
"""
from requests import Response


class ErrorHandler:
    __raise_for_status: bool

    def __init__(self, raise_for_status: bool = False):
        self.__raise_for_status = raise_for_status


    def handler(self, response: Response, *args, **kwargs) -> Response:

        if response.status_code >= 400:
            response.reason = "The request is missing a mandatory request parameter, a parameter contains data which is incorrectly formatted, or the API doesn't have enough information to determine the identity of the customer."
        elif response.status_code == 401:
            response.reason = "There is no authorization information included in the request, the authorization information is incorrect, or the user is not authorized"
        elif response.status_code == 404:
            response.status = "The campaign ID or threat ID does not exist."
        elif response.status_code == 429:
            response.reason = "The user has made too many requests over the past 24 hours and has been throttled."
        elif response.status_code == 500:
            response.reason = "The service has encountered an unexpected situation and is unable to give a better response to the request"

        if self.__raise_for_status:
            response.raise_for_status()

        return response

    @property
    def raise_for_status(self) -> bool:
        return self.__raise_for_status

    @raise_for_status.setter
    def raise_for_status(self, raise_for_status: bool):
        self.__raise_for_status = raise_for_status
