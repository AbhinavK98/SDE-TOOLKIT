"""Liskov Substitution Principle (LSP) - Good Example Base Class

This abstract class defines the common behavior for all account types.
Concrete subclasses can add more behavior, but they should still follow the
contract implied by this base class.
"""


from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, balance):
        # Store the account balance.
        self.balance = balance

    @abstractmethod
    def deposit(self, amount):
        # Subclasses must implement deposit behavior.
        pass


# Revision summary:
# - `Account` is a shared base class for different account types.
# - It defines the interface for depositing money.
# - Subclasses must provide concrete deposit behavior.
