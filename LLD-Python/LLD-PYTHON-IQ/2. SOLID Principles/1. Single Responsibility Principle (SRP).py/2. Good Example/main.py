"""Single Responsibility Principle (SRP) - Good Example

This file shows the correct way to organize responsibilities:
- `User` contains only user data and user-related domain logic.
- `UserRepository` contains only persistence logic.
- `main.py` acts only as an orchestrator that connects these two parts.

Because each file has a single responsibility, changes are easier to make
and the code stays cleaner over time.
"""

from user import User
from userRepository import UserRepository


# Create a user domain object. This object holds user information and
# domain behavior, but it does not save itself.
user_obj = User("Anirudh", 30, "info@cyx.com")

# Create a repository object responsible for saving and deleting users.
user_repo = UserRepository("userDB", "root", "root")

# Use the domain object for presentation/business logic.
user_obj.get_user_info()

# Use the persistence object for database operations.
user_repo.save_to_database(user_obj)


# Revision summary:
# - The `main.py` file should not contain business logic or database logic.
# - Its job is to wire together objects that each have a single responsibility.
