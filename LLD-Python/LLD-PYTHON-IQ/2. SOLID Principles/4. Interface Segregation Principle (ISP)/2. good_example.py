"""Interface Segregation Principle (ISP) - Good Example

This file follows ISP by splitting a broad interface into smaller, more
focused interfaces.

- `Workable` defines only the `work()` method.
- `Eatable` defines only the `eat()` method.
- `Robot` implements only `Workable` because robots do not eat.
- `Employee` implements both `Workable` and `Eatable` because employees do
  both kinds of actions.

This design avoids forcing classes to implement methods they do not need.
"""


from abc import ABC, abstractmethod


class Workable(ABC):
    @abstractmethod
    def work(self):
        pass


class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass


class Robot(Workable):
    def work(self):
        print("Robot is working")


class Employee(Workable, Eatable):
    def eat(self):
        print("Employee is eating")

    def work(self):
        print("Employee is working")


# Example usage:
# Robot only works, and employee can both eat and work.
e = Employee()
e.eat()
e.work()


# Revision summary:
# - ISP says keep interfaces small and focused.
# - `Robot` should not implement `eat()` because it cannot eat.
# - `Workable` and `Eatable` separate the two responsibilities.
# - This makes the design more flexible and easier to extend.
