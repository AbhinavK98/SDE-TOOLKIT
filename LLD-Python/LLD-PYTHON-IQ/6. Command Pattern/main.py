"""Command Pattern - Main

This file shows the main runner for the example in the Command Pattern section.
It explains the core idea in simple language and shows how the code works.
"""

from chef import Chef
from burger_order import BurgerOrder
from pizza_order import PizzaOrder
from waiter import Waiter

chef = Chef()
burgerOrder = BurgerOrder(chef)
pizzaOrder = PizzaOrder(chef)

waiter = Waiter()
waiter.take_order(burgerOrder)

# Revision summary:
# - Part of the Command Pattern examples.
# - Shows the main runner for the example.
# - Use this file to review the pattern and understand its purpose.
