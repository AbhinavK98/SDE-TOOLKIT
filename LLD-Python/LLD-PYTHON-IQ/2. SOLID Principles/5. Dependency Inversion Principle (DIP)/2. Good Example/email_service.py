"""Dependency Inversion Principle (DIP) - Good Example Email Service

This class implements the abstract notification channel interface.
High-level modules can use this service through the `NotificationChannel`
abstraction without depending on email-specific details.
"""


from notification_channel import NotificationChannel


class EmailService(NotificationChannel):
    def send(self, message):
        print(f"Sending Email: {message}")


# Revision summary:
# - This class implements the abstraction used by the notification system.
# - It allows high-level code to remain independent of email details.
