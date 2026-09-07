"""Dependency Inversion Principle (DIP) - Bad Example Email Service

This class is a low-level concrete service for sending email messages.
In the bad example, higher-level code depends directly on this concrete class.
That violates DIP because high-level code should depend on abstractions instead
of concrete implementations.
"""


class EmailService:
    def send_email(self, message):
        print(f"Sending Email: {message}")


# Revision summary:
# - This class is a concrete implementation and should not be directly depended
#   on by higher-level modules if following DIP.
# - Use an abstraction instead so the high-level code can work with any
#   notification channel.
