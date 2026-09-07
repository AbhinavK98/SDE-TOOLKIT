"""Ride Sharing Project - Fare Strategy

This file shows the Fare Strategy example in the Ride Sharing Project section.
It explains the core idea in simple language and shows how the code works.
"""

from abc import ABC, abstractmethod
from vehicle import Vehicle


class FareStrategy(ABC):
    @abstractmethod
    def calFare(self, vehicle: Vehicle, distance: float) -> float:
        pass


class StandardFareStrategy(FareStrategy):
    def calFare(self, vehicle, distance):
        return vehicle.get_fare_amount() * distance


class SharedFareStrategy(FareStrategy):
    def calFare(self, vehicle, distance):
        return vehicle.get_fare_amount() * distance * 0.5


class LuxuryFareStrategy(FareStrategy):
    def calFare(self, vehicle, distance):
        return vehicle.get_fare_amount() * distance * 1.5

# Revision summary:
# - Part of the Ride Sharing Project examples.
# - Shows the Fare Strategy example.
# - Use this file to review the pattern and understand its purpose.
