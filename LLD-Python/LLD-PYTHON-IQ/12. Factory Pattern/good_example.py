"""Factory Pattern - Good Example

This file shows the good example implementation in the Factory Pattern section.
It explains the core idea in simple language and shows how the code works.
"""

from abc import ABC, abstractmethod


class Food(ABC):
    @abstractmethod
    def prepare(self):
        pass


class Pizza:
    def prepare(self):
        print("Preparing pizza")


class Burger:
    def prepare(self):
        print("Preparing burger")


class Pasta:
    def prepare(self):
        print("Preparing burger")


class FoodFactory:
    @staticmethod
    def create_food(food_type: str) -> Food:
        if food_type == "pizza":
            return Pizza()
        elif food_type == "burger":
            return Burger()
        elif food_type == "pasta":
            return Pasta()
        else:
            return None


class RestrauntService:
    def create_order(self, food_type: str):
        f = FoodFactory.create_food(food_type)
        if f is None:
            print("Cannot prepare food")
            return None
        f.prepare()
        return f


restraunt_service = RestrauntService()
restraunt_service.create_order("pizza")
restraunt_service.create_order("burger")

# Revision summary:
# - Part of the Factory Pattern examples.
# - Shows the good example implementation.
# - Use this file to review the pattern and understand its purpose.
