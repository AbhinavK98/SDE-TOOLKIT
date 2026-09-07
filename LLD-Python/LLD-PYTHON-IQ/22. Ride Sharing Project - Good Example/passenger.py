"""Ride Sharing Project - Passenger

This file shows the Passenger example in the Ride Sharing Project section.
It explains the core idea in simple language and shows how the code works.
"""

from user import User


class Passenger(User):
    def __init__(self, name, email, location):
        super().__init__(name, email, location)

    def notify(self, msg: str):
        print(f"Notify to passenger({self.name}) = {msg}")

# Revision summary:
# - Part of the Ride Sharing Project examples.
# - Shows the Passenger example.
# - Use this file to review the pattern and understand its purpose.
