"""Liskov Substitution Principle (LSP) - Good Example Savings Account

This class models a savings account and supports both deposit and withdrawal
operations. It follows the base class contracts and can be substituted for
its parent types.
"""


from withdrawable_account import WithdrawableAccount


class SavingsAccount(WithdrawableAccount):
    def __init__(self, amount):
        super().__init__(amount)

    def deposit(self, amount):
        self.balance += amount
        print(f"Amount deposited, current balance = {self.balance}")

    def withdraw(self, amount):
        if self.balance < amount:
            print("Cannot withdraw, not enough balance")
        else:
            self.balance -= amount
            print(f"Amount withdrawn, current balance = {self.balance}")


# Revision summary:
# - SavingsAccount is a valid substitute for WithdrawableAccount.
# - It implements deposit and withdraw in a compatible way.
# - Good LSP designs preserve expected base class behavior.
