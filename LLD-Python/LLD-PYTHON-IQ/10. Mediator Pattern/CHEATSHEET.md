# Mediator Pattern — Cheat Sheet

---

## One-Liner

> Airplanes talking directly to each other creates N² connections. Adding a flight requires updating e...

---

## Intent

Solve **Mediator Pattern** problems through structured object collaboration.

---

## Key Classes

`AirTrafficControl, ControlTower, Airplane`

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
python with_pattern.py
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

1. Problem: Airplanes talking directly to each other creates N² connections. Adding a flight...
2. Analogy: **Air traffic control tower** — planes don't radio each other; they go through t...
3. Run the code
4. Draw class diagram
5. Explain bad vs good

## 📌 1 Minute Revision

**Airplane.send_message → tower.broadcast → others.receive_message**

## 📌 Next Topic

**Singleton Pattern**

