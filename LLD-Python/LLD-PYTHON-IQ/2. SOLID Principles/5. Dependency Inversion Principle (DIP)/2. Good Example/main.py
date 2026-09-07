"""Dependency Inversion Principle (DIP) - Good Example Usage

This file shows how a high-level module can use a concrete notification
implementation through an abstract interface.
"""


from notification_service import NotificationService
from sms_service import SMSService
from email_service import EmailService


# Create a concrete notification channel.
sms_service = SMSService()

# Inject the concrete channel into the high-level notification service.
ns = NotificationService(sms_service)
ns.notify("Hey")


# Revision summary:
# - This file shows DIP in action: the high-level service uses an abstraction.
# - The concrete implementation is provided from outside.
# - You can replace SMSService with EmailService or a new channel easily.
