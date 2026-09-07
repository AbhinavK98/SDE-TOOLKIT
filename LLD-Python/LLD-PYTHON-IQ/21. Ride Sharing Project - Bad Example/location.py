"""Ride Sharing Project - Location

This file shows the Location example in the Ride Sharing Project section.
It explains the core idea in simple language and shows how the code works.
"""

class Location:
    def __init__(self, lat: float, long: float):
        self.__lat: float = lat
        self.__long: float = long

    def get_latitude(self) -> float:
        return self.__lat

    def get_longitude(self) -> float:
        return self.__long

# Revision summary:
# - Part of the Ride Sharing Project examples.
# - Shows the Location example.
# - Use this file to review the pattern and understand its purpose.
