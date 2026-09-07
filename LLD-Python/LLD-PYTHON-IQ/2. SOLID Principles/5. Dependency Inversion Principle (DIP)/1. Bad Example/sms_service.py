"""Dependency Inversion Principle (DIP) - Bad Example SMS Service

This class is a low-level concrete service for sending SMS messages.
Higher-level code should depend on an abstraction instead of this concrete
implementation.
"""


class SMSService:
    def send_sms(self, message):
        print(f"Sending SMS: {message}")


# Revision summary:
# - In a DIP-friendly design, this service would implement an abstract
#   notification interface used by the higher-level module.
# - That prevents the higher-level code from being tied to SMS details.
