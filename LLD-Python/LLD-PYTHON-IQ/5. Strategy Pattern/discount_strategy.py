"""Strategy Pattern - Discount Strategy

This file shows the Discount Strategy example in the Strategy Pattern section.
It explains the core idea in simple language and shows how the code works.
"""

from abc import ABC, abstractmethod


class DiscountStrategy(ABC):
    @abstractmethod
    def calculate_discount(self):
        pass

# Revision summary:
# - Part of the Strategy Pattern examples.
# - Shows the Discount Strategy example.
# - Use this file to review the pattern and understand its purpose.
