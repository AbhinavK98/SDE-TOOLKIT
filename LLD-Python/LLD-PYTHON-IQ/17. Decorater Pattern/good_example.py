"""Decorater Pattern - Good Example

This file shows the good example implementation in the Decorater Pattern section.
It explains the core idea in simple language and shows how the code works.
"""

from abc import ABC, abstractmethod


class Beverage(ABC):
    @abstractmethod
    def get_description(self) -> str:
        pass

    @abstractmethod
    def get_cost(self) -> int:
        pass


class Coffee(Beverage):
    def get_description(self):
        return "Plain coffee"

    def get_cost(self):
        return 20


class AddOnDecorator(Beverage):
    def __init__(self, coffee: "Coffee"):
        self._coffee = coffee

    def get_description(self):
        pass

    def get_cost(self):
        pass


class MilkDecorator(AddOnDecorator):
    def get_description(self):
        return self._coffee.get_description() + ", Milk"

    def get_cost(self):
        return self._coffee.get_cost() + 20


class WhipCreamDecorator(AddOnDecorator):
    def get_description(self):
        return self._coffee.get_description() + ", Whip Cream"

    def get_cost(self):
        return self._coffee.get_cost() + 50


class SugarDecorator(AddOnDecorator):
    def get_description(self):
        return self._coffee.get_description() + ", Sugar"

    def get_cost(self):
        return self._coffee.get_cost() + 5


coffee = Coffee()

coffee = MilkDecorator(coffee)
coffee = WhipCreamDecorator(coffee)
print(coffee.get_description())
print(coffee.get_cost())

# Revision summary:
# - Part of the Decorater Pattern examples.
# - Shows the good example implementation.
# - Use this file to review the pattern and understand its purpose.
