# Decorator Pattern

---

## What problem does this solve?

Coffee + milk + whip + sugar needs combinatorial subclasses: CoffeeWithMilkAndWhipAndSugar.

---

## Why was this pattern introduced?

Without this design, code becomes brittle — every new feature requires editing existing classes. Large applications (Netflix, Uber, banking systems) need **extensible** object structures where components communicate through clear contracts.

---

## Real-world analogy

**Subway sandwich** — start with bread, add toppings one layer at a time. Each topping wraps the previous.

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
17. Decorater Pattern/
├── bad_example.py
├── good_example.py
├── NOTES.md
├── FLOW.md
├── UML.md
├── INTERVIEW.md
└── CHEATSHEET.md
```

| File | Purpose |
|------|--------|
| `bad_example.py` | CoffeeWithMilk fixed combo |
| `good_example.py` | Composable decorators on Coffee |



## Bad vs Good

| Bad | Good |
|-----|------|
| CoffeeWithMilk subclass explosion | MilkDecorator, WhipCreamDecorator wrap Beverage recursively |


## Code Walkthrough

**Key classes:** `Beverage, Coffee, AddOnDecorator, MilkDecorator, WhipCreamDecorator`

Read each Python file in order listed in the folder structure. Every class exists to model one responsibility. Methods define the contract between objects.

> **💡 Interview Tip**
>
> Explain *why* each class exists before explaining *what* it does.

---

## Execution Flow

```bash
cd "17. Decorater Pattern"
python good_example.py
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

Decorator Pattern teaches you to structure objects so systems grow without breaking. Master the **intent**, draw the **diagram**, then read the **code**.


---

## 📌 5 Minute Revision

- **Problem:** See "What problem does this solve?" above
- **Solution:** Study the good example / pattern structure
- **Key classes:** See class diagram
- **Run:** `Python @decorator (different concept!)`

## 📌 1 Minute Revision

> Understand the **why** before the **how**. Draw the diagram, then explain object communication.

## 📌 Related Patterns

Python @decorator (different concept!)

## 📌 Next Topic to Learn

→ **Proxy Pattern**

