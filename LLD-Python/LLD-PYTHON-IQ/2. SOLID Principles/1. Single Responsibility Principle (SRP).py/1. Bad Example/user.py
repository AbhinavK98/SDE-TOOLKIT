"""Single Responsibility Principle (SRP) - Bad Example

This file demonstrates a class that violates SRP. The `User` class has too
many responsibilities:
- It stores user data (name, age, email).
- It prints user information.
- It contains business logic (`is_adult`).
- It performs persistence operations (`save_to_database`,
  `delete_user_from_database`).

A class with multiple responsibilities is harder to maintain. If the way we
save users changes, or the business rules change, this class must be edited
for those unrelated reasons.
"""


class User:
    def __init__(self, name, age, email):
        # Responsibility: user data state
        self.name = name
        self.age = age
        self.email = email

    def get_user_info(self):
        # Responsibility: presentation / display logic
        # This method prints user info directly, which mixes I/O with the model.
        print(f"This is {self.name} and my age is {self.age}")

    def is_adult(self) -> bool:
        # Responsibility: business logic
        return self.age > 18

    def save_to_database(self):
        # Responsibility: persistence
        # This simulates saving to a database, which should belong to a
        # separate data-access class.
        print(f"{self.name} is getting saved to Database")

    def delete_user_from_database(self):
        # Responsibility: persistence
        print(f"{self.name} is getting deleted from Database")


# Revision summary:
# - SRP means a class should have one reason to change.
# - This bad example mixes data, business rules, display, and database logic.
# - The correct design separates these into different classes.
