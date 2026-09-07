"""Liskov Substitution Principle (LSP) - Good Example Withdrawable Base

This class extends the basic account interface by adding withdrawal behavior.
It allows only accounts that support withdrawals to expose that operation.
"""


from account import Account
from abc import abstractmethod


class WithdrawableAccount(Account):
    def __init__(self, balance):
        super().__init__(balance)

    @abstractmethod
    def withdraw(self, amount):
        # Subclasses that support withdrawals must implement this method.
        pass


# Revision summary:
# - WithdrawableAccount adds withdrawal behavior to the base Account.
# - Only accounts that truly support withdrawals should inherit from this.
# - This avoids forcing non-withdrawable accounts to implement withdraw().
