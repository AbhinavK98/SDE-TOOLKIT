# Singleton Pattern — Cheat Sheet

---

## One-Liner

> Multiple Logger instances write to different files or duplicate config. Some resources must exist ex...

---

## Intent

Solve **Singleton Pattern** problems through structured object collaboration.

---

## Key Classes

`Logger`

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

1. Problem: Multiple Logger instances write to different files or duplicate config. Some res...
2. Analogy: **President of a country** — only one at a time. Elections return the same offic...
3. Run the code
4. Draw class diagram
5. Explain bad vs good

## 📌 1 Minute Revision

**Logger('a') → Logger('b') → same instance → shared log_count**

## 📌 Next Topic

**Factory Pattern**

