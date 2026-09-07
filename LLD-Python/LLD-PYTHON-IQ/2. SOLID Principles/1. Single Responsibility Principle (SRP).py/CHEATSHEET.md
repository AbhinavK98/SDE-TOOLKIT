# Single Responsibility Principle (SRP) — Cheat Sheet

---

## One-Liner

> One class doing everything — save to DB, validate, send email — changes for one reason break unrelat...

---

## Intent

Solve **Single Responsibility Principle (SRP)** problems through structured object collaboration.

---

## Key Classes

`User, UserRepository`

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
cd '2. Good Example' && python main.py
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

1. Problem: One class doing everything — save to DB, validate, send email — changes for one ...
2. Analogy: A **chef cooks**, a **waiter serves**. If the chef also handles billing, the kit...
3. Run the code
4. Draw class diagram
5. Explain bad vs good

## 📌 1 Minute Revision

**main creates User → UserRepository.save_to_database(user)**

## 📌 Next Topic

**Open Close Principle (OCP)**

