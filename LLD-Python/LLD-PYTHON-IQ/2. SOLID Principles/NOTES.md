# SOLID Principles — Overview

---

## What problem does SOLID solve?

As codebases grow, small changes cause cascading bugs. **SOLID** is five design rules that keep classes focused, extensible, and safe to substitute — the grammar of maintainable object-oriented design.

---

## The Five Principles

```mermaid
graph LR
    S[SRP] --> O[OCP]
    O --> L[LSP]
    L --> I[ISP]
    I --> D[DIP]
```

| Letter | Principle | One-Line |
|--------|-----------|----------|
| **S** | Single Responsibility | One class, one reason to change |
| **O** | Open/Closed | Open for extension, closed for modification |
| **L** | Liskov Substitution | Subtypes must honor parent contracts |
| **I** | Interface Segregation | No client depends on unused methods |
| **D** | Dependency Inversion | Depend on abstractions, not concretions |

---

## Recommended Study Order

1. [SRP](1.%20Single%20Responsibility%20Principle%20(SRP).py/NOTES.md) — Foundation
2. [OCP](2.%20Open%20Close%20Principle%20(OCP)/NOTES.md) — Leads to Strategy/Factory
3. [LSP](3.%20Liskov%20Substitution%20Principle%20(LSP)/NOTES.md) — Inheritance done right
4. [ISP](4.%20Interface%20Segregation%20Principle%20(ISP)/NOTES.md) — Small interfaces
5. [DIP](5.%20Dependency%20Inversion%20Principle%20(DIP)/NOTES.md) — Production DI

---

## Folder Structure

```
2. SOLID Principles/
├── 1. Single Responsibility Principle (SRP).py/
│   ├── 1. Bad Example/
│   └── 2. Good Example/
├── 2. Open Close Principle (OCP)/
├── 3. Liskov Substitution Principle (LSP)/
├── 4. Interface Segregation Principle (ISP)/
├── 5. Dependency Inversion Principle (DIP)/
└── [NOTES, FLOW, UML, INTERVIEW, CHEATSHEET].md
```

Each principle folder has **bad** and **good** examples side by side.

---

## How Principles Connect to Patterns

| Principle | Pattern That Embodies It |
|-----------|---------------------------|
| SRP | Facade splits orchestration from subsystems |
| OCP | Strategy, Factory — extend without editing |
| LSP | Proper inheritance hierarchies in State |
| ISP | Small ABCs in Adapter, Iterator |
| DIP | Strategy injection, NotificationChannel |

---

## Real-World Analogy

**Hospital departments**

- **SRP:** Cardiology doesn't handle billing
- **OCP:** New treatment protocol without rebuilding the hospital
- **LSP:** Any qualified doctor can substitute in ER
- **ISP:** Nurses don't need surgeon credentials on their ID
- **DIP:** Doctors depend on "lab results interface," not a specific machine brand

---

## Bad vs Good — Cross-Cutting Theme

| Smell | SOLID Fix |
|-------|-----------|
| God class | SRP |
| Giant if/elif | OCP + Strategy |
| Subclass throws on parent method | LSP — split hierarchy |
| Robot forced to implement eat() | ISP |
| Service creates own dependencies | DIP |

---

## Interview Preparation

For each principle, be able to:

1. State the definition in one sentence
2. Give the bad example problem from this repo
3. Explain how the good example fixes it
4. Name a real system where you've seen the violation

See each principle's [INTERVIEW.md](1.%20Single%20Responsibility%20Principle%20(SRP).py/INTERVIEW.md) for detailed Q&A.

---

## Summary

SOLID isn't five random rules — they're a **progression**. Master SRP first. Every design pattern in folders 3–22 assumes you understand at least OCP and DIP.

---

## 📌 5 Minute Revision

**S** — one job · **O** — extend don't edit · **L** — honest subtypes · **I** — small interfaces · **D** — inject abstractions

## 📌 Next Topic

[1. Single Responsibility Principle](1.%20Single%20Responsibility%20Principle%20(SRP).py/NOTES.md)
