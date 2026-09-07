"""Facade Pattern - Good Example

This file shows the good example implementation in the Facade Pattern section.
It explains the core idea in simple language and shows how the code works.
"""

class UserService:
    def login(self, username: str, password: str) -> dict:
        print(f"[UserService] Logging in: {username}")
        return {"user_id": "U123", "name": username}

    def get_profile(self, user_id: str) -> dict:
        print(f"[UserService] Getting profile for: {user_id}")
        return {"user_id": user_id, "name": "Rahul", "address": "Mumbai"}


class OrderService:
    def get_orders(self, user_id: str) -> list:
        print(f"[OrderService] Getting orders for: {user_id}")
        return [
            {"order_id": "ORD-1", "total": 1500},
            {"order_id": "ORD-2", "total": 3000},
        ]


class ApiGateway:
    def __init__(self):
        self.__user_service = UserService()
        self.__order_service = OrderService()

    def login_user(self, username, password):
        self.__user_service.login(username, password)

    def get_user_profile(self, user_id):
        self.__user_service.get_profile(user_id)

    def get_order_details(self, user_id):
        self.__order_service.get_orders(user_id)

    def get_all_details(self, user_id, username, password):
        self.__user_service.login(username, password)
        self.__user_service.get_profile(user_id)
        print(self.__order_service.get_orders(user_id))


api_gateway = ApiGateway()
api_gateway.get_all_details("d23e32", "test", "123")

# Revision summary:
# - Part of the Facade Pattern examples.
# - Shows the good example implementation.
# - Use this file to review the pattern and understand its purpose.
