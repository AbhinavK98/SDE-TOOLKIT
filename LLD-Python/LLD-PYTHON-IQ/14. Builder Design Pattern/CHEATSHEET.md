# Builder Pattern — Cheat Sheet

---

## One-Liner

> Laptop with 5 optional params needs telescoping constructors: Laptop(cpu, ram, None, None, screen)....

---

## Intent

Solve **Builder Pattern** problems through structured object collaboration.

---

## Key Classes

`Laptop, LaptopBuilder`

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

1. Problem: Laptop with 5 optional params needs telescoping constructors: Laptop(cpu, ram, N...
2. Analogy: **Custom Starbucks drink** — size, milk, shots, syrup — built step by step, not ...
3. Run the code
4. Draw class diagram
5. Explain bad vs good

## 📌 1 Minute Revision

**LaptopBuilder().set_processor().set_ram().build()**

## 📌 Next Topic

**Prototype Pattern**

