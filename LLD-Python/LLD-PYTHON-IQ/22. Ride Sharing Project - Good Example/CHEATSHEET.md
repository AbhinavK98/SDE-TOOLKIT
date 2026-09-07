# Ride Sharing — Cheat Sheet

---

## One-Liner

> Production ride-sharing needs matching, fare strategies, ride lifecycle, notifications, and extensib...

---

## Intent

Solve **Ride Sharing** problems through structured object collaboration.

---

## Key Classes

`User, Driver, Passenger, Vehicle, Car, Bike, FareStrategy, Ride, RideMatchingService`

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

1. Problem: Production ride-sharing needs matching, fare strategies, ride lifecycle, notific...
2. Analogy: **Uber's architecture** — passengers, drivers, vehicles, pricing engine, ride st...
3. Run the code
4. Draw class diagram
5. Explain bad vs good

## 📌 1 Minute Revision

**requestRide → find driver → create Ride → calculate fare → notify → complete → return driver**

## 📌 Next Topic

**Mock LLD interviews**

