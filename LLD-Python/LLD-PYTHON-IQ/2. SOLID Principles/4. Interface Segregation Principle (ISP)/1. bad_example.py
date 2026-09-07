"""Interface Segregation Principle (ISP) - Bad Example

This file demonstrates a violation of ISP. ISP says that clients should not
be forced to depend on interfaces they do not use.

Why this is bad:
- The `Employee` interface requires both `eat()` and `work()`.
- `Worker` can implement both methods cleanly.
- `Robot` cannot eat, but it is still forced to provide an `eat()` method.
- This leads to awkward or incorrect implementations and makes the interface
  too broad.
"""


from abc import ABC, abstractmethod


class Employee(ABC):
    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def work(self):
        pass


class Worker(Employee):
    def eat(self):
        print("Worker is eating")

    def work(self):
        print("Worker is working")


class Robot(Employee):
    def work(self):
        print("Robot is working")

    def eat(self):
        # This is a problem. Robot should not need to implement `eat()`.
        raise Exception("Robot cant eat")


r = Robot()
r.eat()


# Revision summary:
# - ISP says interfaces should be small and specific.
# - A class should not be forced to implement methods it does not need.
# - In this bad example, `Robot` is forced to implement `eat()` even though it
#   cannot eat.
# - This makes the code less clean and harder to maintain.
