"""Ride Sharing Project - Ride

This file shows the Ride example in the Ride Sharing Project section.
It explains the core idea in simple language and shows how the code works.
"""

from enum import Enum
from passenger import Passenger
from driver import Driver
from fare_strategy import FareStrategy


class RideStatus(Enum):
    SCHEDULED = "SCHEDULED"
    ONGOING = "ONGOING"
    COMPLETED = "COMPLETED"


class Ride:
    def __init__(
        self,
        passenger: "Passenger",
        driver: "Driver",
        distance: float,
        fare_strategy: "FareStrategy",
    ):
        self.passenger = passenger
        self.driver = driver
        self.distance = distance
        self.fare_strategy = fare_strategy
        self.fare: float = 0.0
        self.status: RideStatus = RideStatus.SCHEDULED

    def calculateFare(self):
        self.fare = self.fare_strategy.calFare(self.driver.get_vehicle(), self.distance)

    def getRideFare(self):
        return self.fare

    def updateStatus(self, new_ride_status: RideStatus):
        self.status = new_ride_status
        self.__notifyUsers(self.status)

    def __notifyUsers(self, ride_status: RideStatus):
        self.driver.notify(f"Your ride is {ride_status.value}")
        self.passenger.notify(f"Your ride status is {ride_status.value}")

# Revision summary:
# - Part of the Ride Sharing Project examples.
# - Shows the Ride example.
# - Use this file to review the pattern and understand its purpose.
