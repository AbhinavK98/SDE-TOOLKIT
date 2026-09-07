"""Command Pattern - Burger Order

This file shows the Burger Order example in the Command Pattern section.
It explains the core idea in simple language and shows how the code works.
"""

from order import Order
from chef import Chef


class BurgerOrder(Order):
    def __init__(self, chef: Chef):
        self.__chef = chef

    def execute(self):
        print("Burger Order")
        self.__chef.cook_burger()

# Revision summary:
# - Part of the Command Pattern examples.
# - Shows the Burger Order example.
# - Use this file to review the pattern and understand its purpose.
