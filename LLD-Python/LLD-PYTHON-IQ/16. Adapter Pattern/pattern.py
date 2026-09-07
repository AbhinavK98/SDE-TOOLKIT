"""Adapter Pattern - Pattern

This file shows the Pattern example in the Adapter Pattern section.
It explains the core idea in simple language and shows how the code works.
"""

from abc import ABC, abstractmethod


# Interface
class NotificationService(ABC):
    @abstractmethod
    def send(self, to: str, title: str, body: str):
        pass


class EmailNotificationService(NotificationService):
    def send(self, to: str, title: str, body: str):
        print("\nSending Email through EmailNotificationSerivce")
        print(f"To = {to}")
        print(f"Title = {title}")
        print(f"Body = {body}")


class SendGridEmailService:
    def send_email(self, recipient: str, subject: str, content: str):
        print("\nSending Email through SendGridEmailService")
        print(f"Recipient = {recipient}")
        print(f"Subject = {subject}")
        print(f"Content = {content}")


class SendGridAdapter(NotificationService):
    def __init__(self, send_grid_service: SendGridEmailService):
        self.__send_grid_service = send_grid_service

    def send(self, to: str, title: str, body: str):
        self.__send_grid_service.send_email(to, title, body)


class OrderService:
    def __init__(self, email_service: "NotificationService"):
        self.__email_service = email_service

    def create_order(self):
        self.__email_service.send(
            "info@codeanddebug.in", "New Order", "Order has been placed"
        )


# email_notification_service = EmailNotificationService()
# order_service = OrderService(email_notification_service)
# order_service.create_order()

send_grid_service = SendGridEmailService()
send_grid_adapter = SendGridAdapter(send_grid_service)
order_service = OrderService(send_grid_adapter)
order_service.create_order()

# Revision summary:
# - Part of the Adapter Pattern examples.
# - Shows the Pattern example.
# - Use this file to review the pattern and understand its purpose.
