"""Liskov Substitution Principle (LSP) - Good Example Usage

This file shows how different account classes can be used in a consistent way.
The code should work regardless of which concrete account subtype is used.
"""


from savings_account import SavingsAccount
from fixed_deposit import FixedDepositAccount


# Create a regular savings account and use it.
# s = SavingsAccount(1000)
# s.deposit(1000)
# s.withdraw(500)

# Create a fixed deposit account and use it.
fd = FixedDepositAccount(1000)
fd.deposit(1000)


# Revision summary:
# - This entry point shows how account objects are used in practice.
# - Good LSP designs let you swap account types without surprising behavior.
# - The concrete classes should behave consistently with their base type.
