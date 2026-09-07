"""Ride Sharing Project - User

This file shows the User example in the Ride Sharing Project section.
It explains the core idea in simple language and shows how the code works.
"""

from location import Location
from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self, name: str, email: str, location: Location):
        self.name = name
        self.email = email
        self.location = location

    def get_location(self):
        return self.location

    def set_location(self, new_location: Location):
        self.location = new_location

    @abstractmethod
    def notify(self):
        pass

# Revision summary:
# - Part of the Ride Sharing Project examples.
# - Shows the User example.
# - Use this file to review the pattern and understand its purpose.
