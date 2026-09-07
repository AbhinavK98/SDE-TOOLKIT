"""Ride Sharing Project - Ride Matching Service

This file shows the Ride Matching Service example in the Ride Sharing Project section.
It explains the core idea in simple language and shows how the code works.
"""

from typing import List
from driver import Driver
from passenger import Passenger
from location import Location
from fare_strategy import FareStrategy
from ride import Ride, RideStatus


class RideMatchingService:
    def __init__(self):
        self.__available_drivers: List[Driver] = []

    def add_driver(self, driver: Driver):
        self.__available_drivers.append(driver)

    def requestRide(
        self, passenger: Passenger, distance: float, strategy: FareStrategy
    ):
        if len(self.__available_drivers) == 0:
            passenger.notify("No Drivers available")
            return

        # Nearest Driver
        nearestDriver: Driver = self.__findNearestDriver(passenger.get_location())
        self.__available_drivers.remove(nearestDriver)

        ride: Ride = Ride(passenger, nearestDriver, distance, strategy)
        ride.calculateFare()

        passenger.notify(f"Ride scheduled with fare Rs.{ride.getRideFare()}")
        nearestDriver.notify(f"You have one new ride for Rs{ride.getRideFare()}")

        ride.updateStatus(RideStatus.ONGOING)

        # After SOmetime
        ride.updateStatus(RideStatus.COMPLETED)
        self.__available_drivers.append(nearestDriver)
        return

    def __findNearestDriver(self, passenger_location: Location) -> Driver:
        assignedDriver = None
        minDistance = float("inf")
        for driver in self.__available_drivers:
            dist = driver.get_location().calcDistance(passenger_location)
            if dist < minDistance:
                minDistance = dist
                assignedDriver = driver
        return assignedDriver

# Revision summary:
# - Part of the Ride Sharing Project examples.
# - Shows the Ride Matching Service example.
# - Use this file to review the pattern and understand its purpose.
