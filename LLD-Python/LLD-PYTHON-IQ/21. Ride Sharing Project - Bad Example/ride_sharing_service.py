"""Ride Sharing Project - Ride Sharing Service

This file shows the Ride Sharing Service example in the Ride Sharing Project section.
It explains the core idea in simple language and shows how the code works.
"""

from typing import List
from driver import Driver
from passenger import Passenger
from location import Location
from math import sqrt
from vehicle import Vehicle


class RideSharingServiceApp:
    def __init__(self):
        self.drivers: List[Driver] = []
        self.passengers: List[Passenger] = []

    # Method to add driver
    def add_driver(self, driver: Driver):
        self.drivers.append(driver)

    # Method to add a passenger
    def add_passenger(self, passenger: Passenger):
        self.passengers.append(passenger)

    def __calcFare(self, vehicle: Vehicle, distance: float):
        if vehicle.type == "Car":
            return distance * 20
        elif vehicle.type == " Bike":
            return distance * 12
        else:
            return distance * 8

    def bookRide(self, passenger: Passenger, distance: float):
        # Edge case
        if len(self.drivers) == 0:
            print(f"No drivers available for {passenger.name}")
            return
        # Hard coded logic assignemnt
        # Find the nearest driver
        # O(n) - Brute Force
        assignedDriver = None
        minDistance = float("inf")
        for driver in self.drivers:
            currentDriverDistance = self.__calcDistance(
                passenger.location, driver.location
            )
            if currentDriverDistance < minDistance:
                minDistance = currentDriverDistance
                assignedDriver = driver

        # Fare Calculate
        expectedFare: float = self.__calcFare(assignedDriver.vehicle, distance)

        # Check if the driver is ASSIGNED/AVAILABLE
        # TODO

        # Show he driver and fare to the passenger
        print(
            f"Ride booked for {passenger.name} with driver {assignedDriver.name} with fare of Rs.{expectedFare}"
        )
        print(f"Driver is on the way and is {minDistance:.2f}km away")

# Revision summary:
# - Part of the Ride Sharing Project examples.
# - Shows the Ride Sharing Service example.
# - Use this file to review the pattern and understand its purpose.
