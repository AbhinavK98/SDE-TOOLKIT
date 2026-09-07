"""Ride Sharing Project - Vehicle

This file shows the Vehicle example in the Ride Sharing Project section.
It explains the core idea in simple language and shows how the code works.
"""

from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, number_plate: str):
        self.number_plate: str = number_plate

    @abstractmethod
    def get_fare_amount(self) -> float:
        pass

# Revision summary:
# - Part of the Ride Sharing Project examples.
# - Shows the Vehicle example.
# - Use this file to review the pattern and understand its purpose.
