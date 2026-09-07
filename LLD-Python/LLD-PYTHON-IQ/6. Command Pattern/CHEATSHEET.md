# Command Pattern — Cheat Sheet

---

## One-Liner

> Waiter shouldn't know how to cook pizza vs burger. Order placement and execution must be decoupled f...

---

## Intent

Solve **Command Pattern** problems through structured object collaboration.

---

## Key Classes

`Order, PizzaOrder, BurgerOrder, Chef, Waiter`

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

1. Problem: Waiter shouldn't know how to cook pizza vs burger. Order placement and execution...
2. Analogy: **Restaurant order ticket** — waiter writes order; chef executes later. Ticket i...
3. Run the code
4. Draw class diagram
5. Explain bad vs good

## 📌 1 Minute Revision

**Waiter.take_order(BurgerOrder) → execute() → chef.cook_burger()**

## 📌 Next Topic

**Template Pattern**

