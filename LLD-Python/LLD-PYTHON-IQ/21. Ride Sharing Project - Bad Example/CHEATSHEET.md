# Ride Sharing — Cheat Sheet

---

## One-Liner

> Monolithic RideSharingServiceApp with hardcoded fares, missing distance calc, no ride lifecycle — ty...

---

## Intent

Solve **Ride Sharing** problems through structured object collaboration.

---

## Key Classes

`Location, Vehicle, Driver, Passenger, RideSharingServiceApp`

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
python client.py
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

1. Problem: Monolithic RideSharingServiceApp with hardcoded fares, missing distance calc, no...
2. Analogy: A **taxi dispatcher** who is also the accountant, mechanic, and GPS — one person...
3. Run the code
4. Draw class diagram
5. Explain bad vs good

## 📌 1 Minute Revision

**client → bookRide → find driver → calc fare (broken distance)**

## 📌 Next Topic

**Ride Sharing Good Example**

