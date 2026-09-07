"""Oops Recap - Classes Objects

This file shows the Classes Objects example in the Oops Recap section.
It explains the core idea in simple language and shows how the code works.
"""

class Student:
    # Methods
    def __init__(self, name: str, age: int, gender: str) -> None:
        # Attributes
        self.name = name
        self.age = age
        self.gender = gender

    def display(self) -> None:
        print(f"My name is {self.name}, age is {self.age} and gender is {self.gender}")

    def get_age(self) -> int:
        return self.age


s1 = Student("Anirudh", 22, "Male")
print(s1.get_age())

# Revision summary:
# - Part of the Oops Recap examples.
# - Shows the Classes Objects example.
# - Use this file to review the pattern and understand its purpose.
