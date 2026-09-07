"""Command Pattern - Waiter

This file shows the Waiter example in the Command Pattern section.
It explains the core idea in simple language and shows how the code works.
"""

from order import Order


class Waiter:
    def take_order(self, order: Order):
        order.execute()

# Revision summary:
# - Part of the Command Pattern examples.
# - Shows the Waiter example.
# - Use this file to review the pattern and understand its purpose.
