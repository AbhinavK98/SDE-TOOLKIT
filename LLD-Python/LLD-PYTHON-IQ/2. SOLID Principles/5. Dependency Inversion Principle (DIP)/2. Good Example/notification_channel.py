"""Dependency Inversion Principle (DIP) - Good Example Notification Channel

This file defines the abstraction used by high-level modules.
The `NotificationChannel` interface ensures that the notification system
depends on a general contract rather than on concrete services.
"""


from abc import ABC, abstractmethod


class NotificationChannel(ABC):
    @abstractmethod
    def send(self, message):
        pass


# Revision summary:
# - This interface is the abstraction that both email and SMS services can
#   implement.
# - High-level modules should use this abstract type instead of concrete
#   implementations.
