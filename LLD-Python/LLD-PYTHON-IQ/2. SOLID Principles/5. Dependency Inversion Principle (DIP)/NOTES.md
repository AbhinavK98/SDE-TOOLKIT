# Dependency Inversion Principle (DIP)

---

## What problem does this solve?

High-level `NotificationService` directly creates `EmailService` and `SMSService` — can't swap channels without editing service.

---

## Why was this pattern introduced?

Without this design, code becomes brittle — every new feature requires editing existing classes. Large applications (Netflix, Uber, banking systems) need **extensible** object structures where components communicate through clear contracts.

---

## Real-world analogy

A **CEO** doesn't solder circuit boards. They depend on an **IT abstraction**; the concrete vendor can change.

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
2. SOLID Principles/5. Dependency Inversion Principle (DIP)/
├── 1. Bad Example/
├── 2. Good Example/notification_channel.py
├── 2. Good Example/notification_service.py
├── 2. Good Example/main.py
├── NOTES.md
├── FLOW.md
├── UML.md
├── INTERVIEW.md
└── CHEATSHEET.md
```

| File | Purpose |
|------|--------|
| `1. Bad Example/` | notification_service creates concrete deps |
| `2. Good Example/notification_channel.py` | Abstract channel |
| `2. Good Example/notification_service.py` | Depends on injected channel |
| `2. Good Example/main.py` | Composition root — wires SMS |



## Bad vs Good

| Bad | Good |
|-----|------|
| NotificationService constructs EmailService/SMSService internally | NotificationChannel ABC; inject SMSService or EmailService via constructor |


## Code Walkthrough

**Key classes:** `NotificationChannel, EmailService, SMSService, NotificationService`

Read each Python file in order listed in the folder structure. Every class exists to model one responsibility. Methods define the contract between objects.

> **💡 Interview Tip**
>
> Explain *why* each class exists before explaining *what* it does.

---

## Execution Flow

```bash
cd "5. Dependency Inversion Principle (DIP)"
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

Dependency Inversion Principle (DIP) teaches you to structure objects so systems grow without breaking. Master the **intent**, draw the **diagram**, then read the **code**.


---

## 📌 5 Minute Revision

- **Problem:** See "What problem does this solve?" above
- **Solution:** Study the good example / pattern structure
- **Key classes:** Strategy, Factory, DI in production apps
- **Run:** `Strategy, Factory, DI in production apps`

## 📌 1 Minute Revision

> Understand the **why** before the **how**. Draw the diagram, then explain object communication.

## 📌 Related Patterns

Strategy, Factory, DI in production apps

## 📌 Next Topic to Learn

→ **Memento Pattern**

