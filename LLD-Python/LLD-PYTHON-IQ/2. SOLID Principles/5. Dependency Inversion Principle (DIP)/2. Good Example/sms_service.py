"""Dependency Inversion Principle (DIP) - Good Example SMS Service

This class also implements the notification channel abstraction.
It can be used interchangeably with other notification services.
"""


from notification_channel import NotificationChannel


class SMSService(NotificationChannel):
    def send(self, message):
        print(f"Sending SMS: {message}")


# Revision summary:
# - SMSService follows the same interface as EmailService.
# - This allows different notification channels to be swapped easily.
