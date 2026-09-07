"""Strategy Pattern - Diawli

This file shows the Diawli example in the Strategy Pattern section.
It explains the core idea in simple language and shows how the code works.
"""

from discount_strategy import DiscountStrategy


class DiwaliStrategy(DiscountStrategy):
    def calculate_discount(self):
        print("Applying diwali discount of 20%")

# Revision summary:
# - Part of the Strategy Pattern examples.
# - Shows the Diawli example.
# - Use this file to review the pattern and understand its purpose.
