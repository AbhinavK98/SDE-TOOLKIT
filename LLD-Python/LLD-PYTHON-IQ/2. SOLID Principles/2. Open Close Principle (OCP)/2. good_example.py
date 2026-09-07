"""Open/Closed Principle - Good Example

This design follows OCP by depending on abstractions and allowing new payment
types without modifying existing code.

How it meets OCP:
- `PaymentMethod` is an abstract base class that defines a `pay` method.
- Each concrete payment method implements `pay` in its own class.
- `PaymentProcessor` depends on the `PaymentMethod` abstraction and works with
  any implementation.
- Adding a new payment type only requires a new class, not changing the
  existing processor.
"""


from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount: int):
        # The contract for payment methods.
        pass


class UPIPayment(PaymentMethod):
    def pay(self, amount: int):
        print(f"Paying through UPI of Rs.{amount}")


class DebitCardPayment(PaymentMethod):
    def pay(self, amount: int):
        print(f"Paying through debit card of Rs.{amount}")


class CreditCardPayment(PaymentMethod):
    def pay(self, amount: int):
        print(f"Paying through credit card of Rs.{amount}")


class PaymentProcessor:
    # This class is closed for modification because it does not need to know
    # every payment type. It simply uses the common `PaymentMethod` interface.
    def process_payment(self, payment_method: PaymentMethod, amount: int):
        payment_method.pay(amount)


# Usage example:
# Create specific payment method objects and pass them to the processor.
debit = DebitCardPayment()
credit = CreditCardPayment()

paym_process = PaymentProcessor()
paym_process.process_payment(debit, 500)


# Revision summary:
# - In OCP-compliant code, new behavior is added by extension, not by editing
#   existing classes.
# - `PaymentProcessor` is closed for modification and open for extension.
# - Concrete payment classes are the extension points.
# - This makes the system flexible and easier to grow.
