"""Ride Sharing Project - Client

This file shows the Client example in the Ride Sharing Project section.
It explains the core idea in simple language and shows how the code works.
"""

from location import Location
from car import Car
from bike import Bike
from driver import Driver
from passenger import Passenger
from ride_matching_service import RideMatchingService
from fare_strategy import LuxuryFareStrategy

loc1 = Location(15.3243, 81.2312)
loc2 = Location(16.6541, 82.8242)
loc3 = Location(15.9812, 82.8483)

car = Car("CS9999")
bike = Bike("PQ4211")

driver1 = Driver("Alice", "abc@example.com", loc2, car)

passenger1 = Passenger("Anirudh", "anirudh@gmail.com", loc2)

ride_matching_service = RideMatchingService()
ride_matching_service.add_driver(driver1)
ride_matching_service.requestRide(passenger1, 50, LuxuryFareStrategy())

# Revision summary:
# - Part of the Ride Sharing Project examples.
# - Shows the Client example.
# - Use this file to review the pattern and understand its purpose.
