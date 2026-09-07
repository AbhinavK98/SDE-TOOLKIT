# Template Method Pattern — Cheat Sheet

---

## One-Liner

> CSV and JSON parsers share open-parse-close steps but differ only in parsing. Duplicating the skelet...

---

## Intent

Solve **Template Method Pattern** problems through structured object collaboration.

---

## Key Classes

`DataParser, CSVParser`

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
python pattern.py
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

1. Problem: CSV and JSON parsers share open-parse-close steps but differ only in parsing. Du...
2. Analogy: **McDonald's franchise** — same steps (prep, cook, serve); only the recipe (pars...
3. Run the code
4. Draw class diagram
5. Explain bad vs good

## 📌 1 Minute Revision

**CSVParser.parse() → _open → _dataParser → _close**

## 📌 Next Topic

**Iterator Pattern**

