"""
This code was tested against Python 3.9
 
Author: Ludvik Jerabek
Package: tap_api
License: MIT
"""

from tap_api.v2.endpoints.campaign import Campaign
from tap_api.v2.endpoints.forensics import Forensics
from tap_api.v2.endpoints.people import People
from tap_api.v2.endpoints.threats import tThreat
from tap_api.v2.endpoints.siem import Siem
from tap_api.v2.endpoints.url import Url

__all__ = ['Campaign', 'Forensics', 'People', 'tThreat.py', 'Siem', 'Url']






