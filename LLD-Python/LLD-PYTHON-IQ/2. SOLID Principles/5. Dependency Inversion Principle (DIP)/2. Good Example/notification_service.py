"""Dependency Inversion Principle (DIP) - Good Example Notification Service

This class depends on the `NotificationChannel` abstraction instead of a
specific service. This is the key idea of DIP.

The concrete channel is injected from outside, so NotificationService does not
need to change when new channels are added.
"""


from notification_channel import NotificationChannel


class NotificationService:
    def __init__(self, channel: NotificationChannel):
        # Dependency injection of the abstraction.
        self.channel = channel

    def notify(self, message):
        self.channel.send(message)


# Revision summary:
# - This service depends on an interface, not on a concrete class.
# - That makes the class flexible and easy to extend.
# - New notification channels can be added without modifying this code.
