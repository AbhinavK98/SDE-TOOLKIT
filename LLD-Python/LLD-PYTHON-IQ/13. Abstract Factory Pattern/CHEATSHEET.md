# Abstract Factory Pattern — Cheat Sheet

---

## One-Liner

> Restaurant must serve consistent cuisine families — North Indian starter+main+dessert together. One ...

---

## Intent

Solve **Abstract Factory Pattern** problems through structured object collaboration.

---

## Key Classes

`Starter, MainCourse, Dessert, CuisineFactory, NorthIndianCuisine`

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

1. Problem: Restaurant must serve consistent cuisine families — North Indian starter+main+de...
2. Analogy: **IKEA room sets** — pick Scandinavian vs Industrial; get matching sofa, table, ...
3. Run the code
4. Draw class diagram
5. Explain bad vs good

## 📌 1 Minute Revision

**RestaurantService(NorthIndianCuisine) → create_meal → prepare all three**

## 📌 Next Topic

**Builder Pattern**

