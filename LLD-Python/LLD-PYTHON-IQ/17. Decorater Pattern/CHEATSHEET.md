# Decorator Pattern — Cheat Sheet

---

## One-Liner

> Coffee + milk + whip + sugar needs combinatorial subclasses: CoffeeWithMilkAndWhipAndSugar....

---

## Intent

Solve **Decorator Pattern** problems through structured object collaboration.

---

## Key Classes

`Beverage, Coffee, AddOnDecorator, MilkDecorator, WhipCreamDecorator`

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
python good_example.py
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

1. Problem: Coffee + milk + whip + sugar needs combinatorial subclasses: CoffeeWithMilkAndWh...
2. Analogy: **Subway sandwich** — start with bread, add toppings one layer at a time. Each t...
3. Run the code
4. Draw class diagram
5. Explain bad vs good

## 📌 1 Minute Revision

**Coffee → MilkDecorator → WhipCreamDecorator → get_cost()**

## 📌 Next Topic

**Proxy Pattern**

