"""Strategy Pattern - Discount Service

This file shows the Discount Service example in the Strategy Pattern section.
It explains the core idea in simple language and shows how the code works.
"""

from discount_strategy import DiscountStrategy


class DiscountService:
    def __init__(self, discount_strategy: DiscountStrategy):
        self.__strategy = discount_strategy

    def set_strategy(self, new_discount_strategy: DiscountStrategy):
        self.__strategy = new_discount_strategy

    def process(self):
        self.__strategy.calculate_discount()

# Revision summary:
# - Part of the Strategy Pattern examples.
# - Shows the Discount Service example.
# - Use this file to review the pattern and understand its purpose.
