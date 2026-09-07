# Single Responsibility Principle (SRP)

---

## What problem does this solve?

One class doing everything — save to DB, validate, send email — changes for one reason break unrelated features.

---

## Why was this pattern introduced?

Without this design, code becomes brittle — every new feature requires editing existing classes. Large applications (Netflix, Uber, banking systems) need **extensible** object structures where components communicate through clear contracts.

---

## Real-world analogy

A **chef cooks**, a **waiter serves**. If the chef also handles billing, the kitchen slows down when payment rules change.

---

## Where is this used?

| Domain | Example |
|--------|---------|
| Tech | Google, Amazon, Uber architectures |
| Finance | Payment processing, account hierarchies |
| Media | Spotify playlists, Netflix recommendations |
| Daily life | Food delivery, hospital systems, libraries |

---

## UML Diagram

```mermaid
classDiagram
    class Client
    class Abstraction {
        <<interface>>
    }
    class Concrete
    Client --> Abstraction
    Abstraction <|.. Concrete
```

> See [UML.md](UML.md) for full diagrams.

---

## Folder Structure

```
2. SOLID Principles/1. Single Responsibility Principle (SRP).py/
├── 1. Bad Example/user.py
├── 2. Good Example/user.py
├── 2. Good Example/userRepository.py
├── 2. Good Example/main.py
├── NOTES.md
├── FLOW.md
├── UML.md
├── INTERVIEW.md
└── CHEATSHEET.md
```

| File | Purpose |
|------|--------|
| `1. Bad Example/user.py` | God class — domain + persistence mixed |
| `2. Good Example/user.py` | Slim User — only user data and is_adult() |
| `2. Good Example/userRepository.py` | Handles save/delete to database |
| `2. Good Example/main.py` | Wires User and UserRepository |



## Bad vs Good

| Bad | Good |
|-----|------|
| `User` class with `save_to_database()`, `delete_user_from_database()`, `is_adult()` | `User` (data + rules), `UserRepository` (persistence), `main.py` (orchestration) |


## Code Walkthrough

**Key classes:** `User, UserRepository`

Read each Python file in order listed in the folder structure. Every class exists to model one responsibility. Methods define the contract between objects.

> **💡 Interview Tip**
>
> Explain *why* each class exists before explaining *what* it does.

---

## Execution Flow

```bash
cd "1. Single Responsibility Principle (SRP).py"
cd '2. Good Example' && python main.py
```

See [FLOW.md](FLOW.md) for step-by-step flow.

---

## Object Interaction

```mermaid
sequenceDiagram
    participant Client
    participant Context
    participant Component
    Client->>Context: request
    Context->>Component: delegate
    Component-->>Client: response
```

---

## Memory Representation

```
Stack                    Heap
─────                    ────
client ref ───────────►  Domain objects
                         linked by references
```

---

## Why is this implementation good?

| Decision | Reason |
|----------|--------|
| Separation of concerns | Each class has one job |
| Abstraction (ABC) | Clients depend on interfaces |
| Encapsulation | Private `__attrs` hide internals |

---

## Advantages

- **Maintainability** — localized changes
- **Testability** — mock dependencies
- **Extensibility** — add classes without editing clients
- **Readability** — clear object roles

## Disadvantages

- **More files** — indirection overhead
- **Learning curve** — beginners may over-apply patterns
- **Over-engineering risk** — don't use patterns for trivial problems

---

## Common Beginner Mistakes

| Mistake | Avoid |
|---------|-------|
| Jumping to patterns without understanding problem | Ask "what breaks without this?" |
| God classes | Split responsibilities (SRP) |
| Ignoring composition | Favor has-a over is-a when appropriate |

---

## Python-Specific Notes

| Feature | Usage |
|---------|-------|
| `abc.ABC` | Interface definition |
| `@abstractmethod` | Force subclass implementation |
| `__` name mangling | Private attributes |
| Type hints | Document contracts |
| `super()` | Parent initialization |

**Python vs Java:** Python uses ABCs or Protocols instead of `interface` keyword. Duck typing works but ABCs are clearer in interviews.

---

## Comparison Table

| Approach | Without Pattern | With Pattern |
|----------|-----------------|--------------|
| Extension | Edit existing code | Add new class |
| Testing | Hard to isolate | Mock interfaces |
| Coupling | High | Low |

---

## Summary

Single Responsibility Principle (SRP) teaches you to structure objects so systems grow without breaking. Master the **intent**, draw the **diagram**, then read the **code**.


---

## 📌 5 Minute Revision

- **Problem:** See "What problem does this solve?" above
- **Solution:** Study the good example / pattern structure
- **Key classes:** Facade, SRP in every pattern folder
- **Run:** `Facade, SRP in every pattern folder`

## 📌 1 Minute Revision

> Understand the **why** before the **how**. Draw the diagram, then explain object communication.

## 📌 Related Patterns

Facade, SRP in every pattern folder

## 📌 Next Topic to Learn

→ **Open Close Principle (OCP)**

