# Facade Pattern — Cheat Sheet

---

## One-Liner

> Mobile app calls login, profile, orders from three services — client knows too much orchestration....

---

## Intent

Solve **Facade Pattern** problems through structured object collaboration.

---

## Key Classes

`UserService, OrderService, ApiGateway`

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

1. Problem: Mobile app calls login, profile, orders from three services — client knows too m...
2. Analogy: **Hotel concierge** — one request: arrange dinner, spa, taxi. You don't call eac...
3. Run the code
4. Draw class diagram
5. Explain bad vs good

## 📌 1 Minute Revision

**api_gateway.get_all_details() → login → profile → orders**

## 📌 Next Topic

**Ride Sharing Bad Example**

