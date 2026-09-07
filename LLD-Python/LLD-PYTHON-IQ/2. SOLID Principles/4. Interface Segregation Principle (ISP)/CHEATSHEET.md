# Interface Segregation Principle (ISP) — Cheat Sheet

---

## One-Liner

> Fat interface forces `Robot` to implement `eat()` which raises Exception — clients depend on methods...

---

## Intent

Solve **Interface Segregation Principle (ISP)** problems through structured object collaboration.

---

## Key Classes

`Workable, Eatable, Robot, Employee`

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

1. Problem: Fat interface forces `Robot` to implement `eat()` which raises Exception — clien...
2. Analogy: A **swiss army knife** interface for a **screwdriver** — you shouldn't need a co...
3. Run the code
4. Draw class diagram
5. Explain bad vs good

## 📌 1 Minute Revision

**Robot.work() — no eat() required**

## 📌 Next Topic

**Dependency Inversion Principle (DIP)**

