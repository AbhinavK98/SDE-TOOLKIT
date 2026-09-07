"""Command Pattern - Pizza Order

This file shows the Pizza Order example in the Command Pattern section.
It explains the core idea in simple language and shows how the code works.
"""

from order import Order
from chef import Chef


class PizzaOrder(Order):
    def __init__(self, chef: Chef):
        self.__chef = chef

    def execute(self):
        print("Pizza Order")
        self.__chef.cook_pizza

# Revision summary:
# - Part of the Command Pattern examples.
# - Shows the Pizza Order example.
# - Use this file to review the pattern and understand its purpose.
