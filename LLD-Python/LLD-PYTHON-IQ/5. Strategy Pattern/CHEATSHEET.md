# Strategy Pattern — Cheat Sheet

---

## One-Liner

> Discount logic buried in if/elif for Diwali, Holi, Christmas — adding festivals means editing the sa...

---

## Intent

Solve **Strategy Pattern** problems through structured object collaboration.

---

## Key Classes

`DiscountStrategy, DiwaliStrategy, HoliStrategy, DiscountService`

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
python main.py
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

1. Problem: Discount logic buried in if/elif for Diwali, Holi, Christmas — adding festivals ...
2. Analogy: **Uber surge pricing** — same ride request, different pricing algorithm swapped ...
3. Run the code
4. Draw class diagram
5. Explain bad vs good

## 📌 1 Minute Revision

**DiscountService(DiwaliStrategy) → process → set_strategy(Holi) → process**

## 📌 Next Topic

**Command Pattern**

