"""Ride Sharing Project - Car

This file shows the Car example in the Ride Sharing Project section.
It explains the core idea in simple language and shows how the code works.
"""

from vehicle import Vehicle


class Car(Vehicle):
    def __init__(self, number_plate):
        super().__init__(number_plate)

    def get_fare_amount(self):
        return 20

# Revision summary:
# - Part of the Ride Sharing Project examples.
# - Shows the Car example.
# - Use this file to review the pattern and understand its purpose.
