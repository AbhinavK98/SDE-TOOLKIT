# Proxy Pattern — Cheat Sheet

---

## One-Liner

> Loading 4 high-res images at gallery open takes 4 seconds. User may only view one....

---

## Intent

Solve **Proxy Pattern** problems through structured object collaboration.

---

## Key Classes

`HighResImage, ImageProxy, PhotoGallery`

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
python good_Example.py.py
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

1. Problem: Loading 4 high-res images at gallery open takes 4 seconds. User may only view on...
2. Analogy: **Netflix thumbnail** — you see preview instantly; full movie loads when you pre...
3. Run the code
4. Draw class diagram
5. Explain bad vs good

## 📌 1 Minute Revision

**add_image (fast) → show_image(2) → load once → cache**

## 📌 Next Topic

**Composite Pattern**

