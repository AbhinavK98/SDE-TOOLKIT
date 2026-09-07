"""Strategy Pattern - Holi

This file shows the Holi example in the Strategy Pattern section.
It explains the core idea in simple language and shows how the code works.
"""

from discount_strategy import DiscountStrategy


class HoliStrategy(DiscountStrategy):
    def calculate_discount(self):
        print("Applying holi discount of 10%")

# Revision summary:
# - Part of the Strategy Pattern examples.
# - Shows the Holi example.
# - Use this file to review the pattern and understand its purpose.
