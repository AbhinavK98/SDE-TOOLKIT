# Dependency Inversion Principle (DIP) — Cheat Sheet

---

## One-Liner

> High-level `NotificationService` directly creates `EmailService` and `SMSService` — can't swap chann...

---

## Intent

Solve **Dependency Inversion Principle (DIP)** problems through structured object collaboration.

---

## Key Classes

`NotificationChannel, EmailService, SMSService, NotificationService`

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

1. Problem: High-level `NotificationService` directly creates `EmailService` and `SMSService...
2. Analogy: A **CEO** doesn't solder circuit boards. They depend on an **IT abstraction**; t...
3. Run the code
4. Draw class diagram
5. Explain bad vs good

## 📌 1 Minute Revision

**main → SMSService → inject into NotificationService → notify()**

## 📌 Next Topic

**Memento Pattern**

