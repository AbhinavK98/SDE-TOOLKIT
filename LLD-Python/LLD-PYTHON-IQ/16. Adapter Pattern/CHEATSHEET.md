# Adapter Pattern — Cheat Sheet

---

## One-Liner

> SendGrid API uses send_email(recipient, subject, content) but your app expects send(to, title, body)...

---

## Intent

Solve **Adapter Pattern** problems through structured object collaboration.

---

## Key Classes

`NotificationService, SendGridAdapter, SendGridEmailService, OrderService`

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

1. Problem: SendGrid API uses send_email(recipient, subject, content) but your app expects s...
2. Analogy: **Power plug adapter** — US plug into EU socket. Same electricity, different int...
3. Run the code
4. Draw class diagram
5. Explain bad vs good

## 📌 1 Minute Revision

**OrderService(adapter) → create_order → adapter.send() → send_grid.send_email()**

## 📌 Next Topic

**Decorator Pattern**

