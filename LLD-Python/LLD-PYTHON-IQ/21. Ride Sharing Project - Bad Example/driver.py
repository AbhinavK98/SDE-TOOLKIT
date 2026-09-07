"""Ride Sharing Project - Driver

This file shows the Driver example in the Ride Sharing Project section.
It explains the core idea in simple language and shows how the code works.
"""

from location import Location
from vehicle import Vehicle


class Driver:
    def __init__(self, name, location: Location, vehicle: Vehicle):
        self.name: str = name
        self.location: Location = location
        self.vehicle: Vehicle = vehicle

    def get_location(self) -> Location:
        return self.location

    def set_location(self, location: Location) -> None:
        self.location = location

# Revision summary:
# - Part of the Ride Sharing Project examples.
# - Shows the Driver example.
# - Use this file to review the pattern and understand its purpose.
