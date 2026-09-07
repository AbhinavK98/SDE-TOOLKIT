"""Single Responsibility Principle (SRP) - Good Example Domain Model

This class is responsible only for storing user data and providing user-related
business logic. It does not perform database operations or manage storage.
"""


class User:
    def __init__(self, name, age, email):
        # Stores user state only.
        self.name = name
        self.age = age
        self.email = email

    def get_user_info(self):
        # Light presentation helper. In stricter designs, even output can
        # be handled elsewhere, but this remains focused on the user object.
        print(f"This is {self.name} and my age is {self.age}")

    def is_adult(self) -> bool:
        # Business rule: determines whether the user is an adult.
        return self.age > 18


# Revision summary:
# - `User` has a single responsibility: user data and related behavior.
# - Persistence is not part of this class.
# - This keeps the domain model clean and easier to test.
