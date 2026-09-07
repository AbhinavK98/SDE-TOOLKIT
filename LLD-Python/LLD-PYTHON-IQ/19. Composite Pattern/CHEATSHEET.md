# Composite Pattern — Cheat Sheet

---

## One-Liner

> File system has files and folders; folders contain files and subfolders. Client shouldn't treat them...

---

## Intent

Solve **Composite Pattern** problems through structured object collaboration.

---

## Key Classes

`FileSystemComponent, File, Folder`

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

1. Problem: File system has files and folders; folders contain files and subfolders. Client ...
2. Analogy: **Organization chart** — CEO manages VPs and individual contributors through sam...
3. Run the code
4. Draw class diagram
5. Explain bad vs good

## 📌 1 Minute Revision

**main_folder.add(file).add(sub_folder.add(file))**

## 📌 Next Topic

**Facade Pattern**

