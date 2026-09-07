# State Pattern — Cheat Sheet

---

## One-Liner

> Transport app with giant if/elif for bike vs walk vs car modes — adding metro means editing every me...

---

## Intent

Solve **State Pattern** problems through structured object collaboration.

---

## Key Classes

`TransportMode, BikeMode, WalkMode, TransportService`

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

1. Problem: Transport app with giant if/elif for bike vs walk vs car modes — adding metro me...
2. Analogy: **Traffic light** — same intersection, behavior changes by state (red/yellow/gre...
3. Run the code
4. Draw class diagram
5. Explain bad vs good

## 📌 1 Minute Revision

**TransportService(BikeMode) → eta() → directions()**

## 📌 Next Topic

**Mediator Pattern**

