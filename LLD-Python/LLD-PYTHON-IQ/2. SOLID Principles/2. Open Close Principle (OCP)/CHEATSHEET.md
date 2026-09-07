# Open/Closed Principle (OCP) — Cheat Sheet

---

## One-Liner

> Every new payment type means editing `PaymentProcessor` with another `elif` — open for modification,...

---

## Intent

Solve **Open/Closed Principle (OCP)** problems through structured object collaboration.

---

## Key Classes

`PaymentProcessor, PaymentMethod, UPIPayment, DebitCardPayment, CreditCardPayment`

---

## When to Use ✅

- System must grow without breaking existing code
- Multiple implementations of same behavior
- Clear interview LLD scenario matches this pattern

## When to Avoid ❌

- Single class, no variation, no growth expected

---

## Run Command

```bash
python 2. good_example.py
```

---

## SOLID Links

| Principle | Connection |
|-----------|------------|
| SRP | One class, one job |
| OCP | Extend, don't modify |
| DIP | Depend on abstractions |

---

## Common Mistakes

- Over-engineering
- Wrong pattern for the problem
- Can't draw UML from memory

---

## 📌 5 Minute Revision

1. Problem: Every new payment type means editing `PaymentProcessor` with another `elif` — op...
2. Analogy: A **power strip** accepts new plugs without rewiring the wall. Your processor sh...
3. Run the code
4. Draw class diagram
5. Explain bad vs good

## 📌 1 Minute Revision

**Create UPIPayment → PaymentProcessor.process_payment(upi, 100)**

## 📌 Next Topic

**Liskov Substitution Principle (LSP)**

