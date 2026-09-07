"""Open/Closed Principle - Bad Example

This `PaymentProcessor` implementation violates the Open/Closed Principle
(OCP). OCP states that software entities should be open for extension but
closed for modification.

Why this is bad:
- `PaymentProcessor.pay` uses `if/elif` statements for each payment type.
- Adding a new payment method requires editing the existing function.
- That means the code is not closed for modification, which makes it less
  stable and harder to extend cleanly.

In a better design, the processor would depend on a generic payment interface
rather than a string value, so new payment types can be added without
changing the existing processor code.
"""


class PaymentProcessor:
    # This method handles all payment types in one place.
    # The problem is that it must change whenever a new type is introduced.
    def pay(self, payment_method: str, amount: int):
        if payment_method == "UPI":
            print(f"Starting UPI transaction of Rs.{amount}")
            print("UPI transaction finished")
        elif payment_method == "credit_card":
            print(f"Starting credit card transaction of Rs.{amount}")
            print("Credit card transaction finished")
        elif payment_method == "net_banking":
            print(f"Starting net banking transaction of Rs.{amount}")
            print("Net Banking transaction finished")


pay_p = PaymentProcessor()
pay_p.pay("credit_card", 500)


# Revision summary:
# - OCP means you should be able to extend behavior without changing existing code.
# - This bad example breaks OCP by hardcoding payment type checks.
# - Every new payment method forces a change in `PaymentProcessor.pay`.
# - This makes the code harder to maintain and more prone to bugs.
