"""Oops Recap - Inheritance

This file shows the Inheritance example in the Oops Recap section.
It explains the core idea in simple language and shows how the code works.
"""

class Animal:
    def __init__(self, name: str, age: int):
        print("Animal INIT")
        self.name = name
        self.age = age

    def eat(self):
        print("I am eating")

    def sleep(self):
        print("I am sleeping")

    def move(self):
        print("I am moving")


class Dog(Animal):
    def __init__(self, name: str, age: int, breed: str):
        super().__init__(name, age)
        self.breed = breed

    def bark(self):
        print("I am barking")

    def display(self):
        print(f"Name is {self.name} and age is {self.age}")

    def move(self):
        print("I am running on 4 legs")


dog = Dog("Cheery", 5, "Indie")
dog.move()

# Revision summary:
# - Part of the Oops Recap examples.
# - Shows the Inheritance example.
# - Use this file to review the pattern and understand its purpose.
