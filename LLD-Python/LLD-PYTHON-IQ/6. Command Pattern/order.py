"""Command Pattern - Order

This file shows the Order example in the Command Pattern section.
It explains the core idea in simple language and shows how the code works.
"""

from abc import ABC, abstractmethod


class Order(ABC):
    @abstractmethod
    def execute(self):
        pass

# Revision summary:
# - Part of the Command Pattern examples.
# - Shows the Order example.
# - Use this file to review the pattern and understand its purpose.
