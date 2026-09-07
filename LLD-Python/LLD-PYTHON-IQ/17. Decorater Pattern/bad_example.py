"""Decorater Pattern - Bad Example

This file shows the bad example implementation in the Decorater Pattern section.
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


class CoffeeWithMilk(Coffee):
    def get_description(self):
        return "Plain coffee with Milk"

    def get_cost(self):
        return 30


coffee1 = Coffee()
print(coffee1.get_description())
print(coffee1.get_cost())

coffee1 = CoffeeWithMilk()
print(coffee1.get_description())
print(coffee1.get_cost())

# Revision summary:
# - Part of the Decorater Pattern examples.
# - Shows the bad example implementation.
# - Use this file to review the pattern and understand its purpose.
