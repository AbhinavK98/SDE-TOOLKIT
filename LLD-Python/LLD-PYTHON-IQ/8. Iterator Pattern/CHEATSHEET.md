# Iterator Pattern — Cheat Sheet

---

## One-Liner

> Client shouldn't know if playlist is array or linked list. Traversal logic shouldn't be duplicated....

---

## Intent

Solve **Iterator Pattern** problems through structured object collaboration.

---

## Key Classes

`Song, Playlist, PlaylistIterator, Node`

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

1. Problem: Client shouldn't know if playlist is array or linked list. Traversal logic shoul...
2. Analogy: **Spotify playlist** — press next regardless of how songs are stored internally....
3. Run the code
4. Draw class diagram
5. Explain bad vs good

## 📌 1 Minute Revision

**add songs → create_iterator → while has_next: next().get_title()**

## 📌 Next Topic

**State Pattern**

