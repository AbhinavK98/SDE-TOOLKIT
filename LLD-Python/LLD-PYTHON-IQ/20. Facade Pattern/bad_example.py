"""Facade Pattern - Bad Example

This file shows the bad example implementation in the Facade Pattern section.
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


user_service = UserService()
order_service = OrderService()


user_service.login("test", "pass")
user_service.get_profile("hjk232322")

print(order_service.get_orders("hjk232322"))

# Revision summary:
# - Part of the Facade Pattern examples.
# - Shows the bad example implementation.
# - Use this file to review the pattern and understand its purpose.
