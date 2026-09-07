"""Factory Pattern - Bad Example

This file shows the bad example implementation in the Factory Pattern section.
It explains the core idea in simple language and shows how the code works.
"""

from abc import ABC, abstractmethod


class Food(ABC):
    @abstractmethod
    def prepare(self):
        pass


class Pizza(Food):
    def prepare(self):
        print("Preparing pizza")


class Burger(Food):
    def prepare(self):
        print("Preparing burger")


# Responsible for making objects
class RestrauntService:
    def create_order(self, food_type: str):
        if food_type == "pizza":
            f = Pizza()
        elif food_type == "burger":
            f = Burger()
        else:
            print("Invalid food type")
            return None
        f.prepare()
        return f


restraunt_service = RestrauntService()
restraunt_service.create_order("pizza")
restraunt_service.create_order("burger")

# Revision summary:
# - Part of the Factory Pattern examples.
# - Shows the bad example implementation.
# - Use this file to review the pattern and understand its purpose.
