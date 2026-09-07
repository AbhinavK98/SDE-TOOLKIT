"""Dependency Inversion Principle (DIP) - Bad Example Notification Service

This file demonstrates a DIP violation.
The `NotificationService` depends directly on concrete services
(`EmailService` and `SMSService`) rather than on an abstract interface.

That means it is hard to replace or extend with new notification channels.
"""


from email_service import EmailService
from sms_service import SMSService


class NotificationService:
    def __init__(self):
        # Directly depends on concrete implementations.
        self.email_service = EmailService()
        self.sms_service = SMSService()

    def notifyByEmail(self, message):
        self.email_service.send_email(message)

    def notifyBySMS(self, message):
        self.sms_service.send_sms(message)


ns = NotificationService()
ns.notifyByEmail("Good morning")
ns.notifyBySMS("Hey")


# Revision summary:
# - DIP says high-level modules should depend on abstractions.
# - This NotificationService depends on concrete classes, not an interface.
# - That couples it tightly to Email and SMS implementations.
# - A better design injects the notification channel abstraction instead.
