"""Liskov Substitution Principle (LSP) - Bad Example

This file shows a violation of LSP. LSP says that subclasses should be
replaceable for their base classes without changing the expected behavior.

Why this is bad:
- `FixedDepositAccount` inherits from `BankAccount` but does not behave like
  a normal bank account because it forbids withdrawals.
- Code that expects a `BankAccount` and calls `withdraw()` would fail when
  given a `FixedDepositAccount`.
- This means the subclass is not a true substitute for the parent.
"""


from abc import ABC, abstractmethod


class BankAccount(ABC):
    def __init__(self, balance: int):
        self.balance: int = balance

    @abstractmethod
    def withdraw(self):
        pass

    @abstractmethod
    def deposit(self):
        pass


class SavingsAccount(BankAccount):
    def __init__(self, balance):
        super().__init__(balance)

    def withdraw(self, amount):
        if self.balance < amount:
            print("Cannot withdraw, not enough balance")
        else:
            self.balance -= amount
            print(f"Amount withdrawn, remaining balance {self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"Amount deposited, remaining balance {self.balance}")


class FixedDepositAccount(BankAccount):
    def __init__(self, balance):
        super().__init__(balance)

    def withdraw(self, amount):
        # Fixed deposit accounts do not allow withdrawal.
        # This breaks the base class contract because `withdraw()` is expected
        # to work on all bank accounts.
        raise Exception("Cannot withdraw from FD")

    def deposit(self, amount):
        self.balance += amount
        print(f"Amount deposited, remaining balance {self.balance}")


# This example fails LSP because `FixedDepositAccount` cannot be used in the
# same way as other `BankAccount` subclasses.
fd = FixedDepositAccount(1000)
fd.deposit(1000)
fd.withdraw(500)


# Revision summary:
# - LSP means subclass objects should be replaceable for base class objects.
# - A FixedDepositAccount should not break the contract of BankAccount.
# - In this bad example, calling withdraw() on a FixedDepositAccount throws
#   an exception, which makes it unsafe to substitute.
