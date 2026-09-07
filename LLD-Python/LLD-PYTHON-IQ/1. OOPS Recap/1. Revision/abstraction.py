"""Oops Recap - Abstraction

This file shows the Abstraction example in the Oops Recap section.
It explains the core idea in simple language and shows how the code works.
"""

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


# Concrete Classes
class Rectangle(Shape):
    def __init__(self, length: int, breadth: int):
        self.length = length
        self.breadth = breadth

    def area(self):
        print(self.length * self.breadth)

    def perimeter(self):
        print(2 * (self.length + self.breadth))


r = Rectangle(5, 2)
r.area()
r.perimeter()

# Revision summary:
# - Part of the Oops Recap examples.
# - Shows the Abstraction example.
# - Use this file to review the pattern and understand its purpose.
