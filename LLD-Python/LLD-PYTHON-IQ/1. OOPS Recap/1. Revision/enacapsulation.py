"""Oops Recap - Enacapsulation

This file shows the Enacapsulation example in the Oops Recap section.
It explains the core idea in simple language and shows how the code works.
"""

class Bank:
    def __init__(self, name: str, balance: int):
        self.name: str = name
        # Private attribute
        self.__balance: int = balance

    # Getter
    def get_balance(self):
        print(f"Current balance = {self.__balance}")

    # Setter
    def set_balance(self, new_amount):
        self.__balance = new_amount

    def __isServerLive(self):
        return True

    def deposit(self, amount: int):
        if self.__isServerLive() == True:
            self.__balance += amount
            print(f"Amount deposited, current balance = {self.__balance}\n")
        else:
            print("Server is down")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Not enought money in bank\n")
        else:
            self.__balance -= amount
            print(f"Amount withdrawn, current balance = {self.__balance}\n")


acc = Bank("Anirudh", 1000)
acc.deposit(1000)
acc.get_balance()
acc.withdraw(500)
acc.__isServerLive()

# Revision summary:
# - Part of the Oops Recap examples.
# - Shows the Enacapsulation example.
# - Use this file to review the pattern and understand its purpose.
