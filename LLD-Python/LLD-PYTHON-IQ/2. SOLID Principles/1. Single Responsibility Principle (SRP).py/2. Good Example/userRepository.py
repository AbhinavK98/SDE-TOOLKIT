"""Single Responsibility Principle (SRP) - Good Example Persistence Layer

This class is responsible only for persistence. It knows how to save and
remove User objects from a data store.

Separating persistence from the domain model keeps the User class focused on
user-specific behavior and prevents storage changes from affecting the
domain model.
"""

from user import User


class UserRepository:
    def __init__(self, db, user, password):
        # Stores connection/configuration details for the persistence layer.
        self.db = db
        self.user = user
        self.password = password

    def save_to_database(self, user: "User"):
        # Persistence responsibility: save the user.
        print(f"{user.name} is getting saved to database")

    def delete_from_database(self, user: "User"):
        # Persistence responsibility: delete the user.
        print(f"{user.name} is getting deleted from database")


# Revision summary:
# - This repository class has one responsibility: persistence.
# - It does not contain business rules or user state logic.
# - That separation makes the system easier to maintain and extend.
