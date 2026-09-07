"""Liskov Substitution Principle (LSP) - Good Example Fixed Deposit

This class represents a fixed deposit account. It matches the contract of the
`Account` base class and only extends behavior in a compatible way.
"""


from account import Account


class FixedDepositAccount(Account):
    def __init__(self, balance):
        super().__init__(balance)

    def deposit(self, amount):
        # This method follows the base class contract for deposit.
        self.balance += amount
        print(f"Amount deposited, current balance = {self.balance}")


# Revision summary:
# - FixedDepositAccount extends Account without breaking the base contract.
# - It implements the required `deposit` method in a normal way.
# - It can be substituted in places expecting an Account.
