"""Ride Sharing Project - Client

This file shows the Client example in the Ride Sharing Project section.
It explains the core idea in simple language and shows how the code works.
"""

from location import Location
from vehicle import Vehicle
from ride_sharing_service import RideSharingServiceApp
from driver import Driver
from passenger import Passenger

loc1 = Location(15.3243, 81.2312)
loc2 = Location(16.6541, 82.8242)
loc3 = Location(15.9812, 82.8483)

car = Vehicle("CS9999", "Car")
bike = Vehicle("PQ4211", "Bike")

driver1 = Driver("Alice", loc2, car)
driver2 = Driver("Bob", loc3, bike)

passenger1 = Passenger("Anirudh", loc1)
passenger2 = Passenger("Vandana", loc2)

ride_sharing_service = RideSharingServiceApp()
ride_sharing_service.add_driver(driver1)
ride_sharing_service.add_driver(driver2)
ride_sharing_service.add_passenger(passenger1)
ride_sharing_service.add_passenger(passenger2)

ride_sharing_service.bookRide(passenger1, 30)
ride_sharing_service.bookRide(passenger2, 50)
ride_sharing_service.bookRide(passenger2, 50)

# Revision summary:
# - Part of the Ride Sharing Project examples.
# - Shows the Client example.
# - Use this file to review the pattern and understand its purpose.
