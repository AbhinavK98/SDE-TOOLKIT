# Memento Pattern — Cheat Sheet

---

## One-Liner

> You need undo without exposing internal state. Saving editor text to a public variable lets anyone c...

---

## Intent

Solve **Memento Pattern** problems through structured object collaboration.

---

## Key Classes

`TextMemento, TextEditor, History`

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

1. Problem: You need undo without exposing internal state. Saving editor text to a public va...
2. Analogy: **Google Docs version history** — restore yesterday's draft without exposing the...
3. Run the code
4. Draw class diagram
5. Explain bad vs good

## 📌 1 Minute Revision

**write → save → write → undo → restore previous state**

## 📌 Next Topic

**Observer Pattern**

