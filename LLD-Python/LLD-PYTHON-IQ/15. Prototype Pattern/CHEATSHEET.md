# Prototype Pattern — Cheat Sheet

---

## One-Liner

> Creating complex ChessBoard from scratch is expensive. Copying shares references — moving a piece on...

---

## Intent

Solve **Prototype Pattern** problems through structured object collaboration.

---

## Key Classes

`ChessPiece, ChessBoard`

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

1. Problem: Creating complex ChessBoard from scratch is expensive. Copying shares references...
2. Analogy: **Photocopy vs snapshot** — shallow copy shares sticky notes; deep copy gives in...
3. Run the code
4. Draw class diagram
5. Explain bad vs good

## 📌 1 Minute Revision

**add pieces → clone() → modify clone → original unchanged**

## 📌 Next Topic

**Adapter Pattern**

