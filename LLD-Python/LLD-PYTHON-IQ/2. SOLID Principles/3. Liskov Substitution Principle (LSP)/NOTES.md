# Liskov Substitution Principle (LSP)

---

## What problem does this solve?

Subclass breaks parent contract — `FixedDepositAccount.withdraw()` raises Exception. Code expecting `BankAccount` crashes.

---

## Why was this pattern introduced?

Without this design, code becomes brittle — every new feature requires editing existing classes. Large applications (Netflix, Uber, banking systems) need **extensible** object structures where components communicate through clear contracts.

---

## Real-world analogy

Every **bird** should fly. If **Penguin** extends Bird but can't fly, the abstraction is wrong. Split `FlyableBird` from `Bird`.

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
2. SOLID Principles/3. Liskov Substitution Principle (LSP)/
├── 1. Bad Example/1. bad_example.py
├── 2. Good Example/account.py
├── 2. Good Example/withdrawable_account.py
├── 2. Good Example/savings_account.py
├── 2. Good Example/fixed_deposit.py
├── 2. Good Example/main.py
├── NOTES.md
├── FLOW.md
├── UML.md
├── INTERVIEW.md
└── CHEATSHEET.md
```

| File | Purpose |
|------|--------|
| `1. Bad Example/1. bad_example.py` | FD violates withdraw contract |
| `2. Good Example/account.py` | Base Account with deposit |
| `2. Good Example/withdrawable_account.py` | Adds withdraw to hierarchy |
| `2. Good Example/savings_account.py` | Full withdrawable account |
| `2. Good Example/fixed_deposit.py` | Deposit only — honest contract |
| `2. Good Example/main.py` | Demo FD usage |



## Bad vs Good

| Bad | Good |
|-----|------|
| FixedDepositAccount inherits withdraw() but throws | Account (deposit only) → WithdrawableAccount adds withdraw(); FD extends Account only |


## Code Walkthrough

**Key classes:** `Account, WithdrawableAccount, SavingsAccount, FixedDepositAccount`

Read each Python file in order listed in the folder structure. Every class exists to model one responsibility. Methods define the contract between objects.

> **💡 Interview Tip**
>
> Explain *why* each class exists before explaining *what* it does.

---

## Execution Flow

```bash
cd "3. Liskov Substitution Principle (LSP)"
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

Liskov Substitution Principle (LSP) teaches you to structure objects so systems grow without breaking. Master the **intent**, draw the **diagram**, then read the **code**.


---

## 📌 5 Minute Revision

- **Problem:** See "What problem does this solve?" above
- **Solution:** Study the good example / pattern structure
- **Key classes:** ISP, inheritance design
- **Run:** `ISP, inheritance design`

## 📌 1 Minute Revision

> Understand the **why** before the **how**. Draw the diagram, then explain object communication.

## 📌 Related Patterns

ISP, inheritance design

## 📌 Next Topic to Learn

→ **Interface Segregation Principle (ISP)**

