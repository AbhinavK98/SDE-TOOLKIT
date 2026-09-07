"""Ride Sharing Project - Driver

This file shows the Driver example in the Ride Sharing Project section.
It explains the core idea in simple language and shows how the code works.
"""

from user import User
from vehicle import Vehicle


class Driver(User):
    def __init__(self, name, email, location, vehicle: Vehicle):
        super().__init__(name, email, location)
        self.__vehicle = vehicle

    def get_vehicle(self) -> Vehicle:
        return self.__vehicle

    def notify(self, msg: str):
        print(f"Notify to driver({self.name}) = {msg}")

# Revision summary:
# - Part of the Ride Sharing Project examples.
# - Shows the Driver example.
# - Use this file to review the pattern and understand its purpose.
