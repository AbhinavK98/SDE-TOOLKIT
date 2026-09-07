# Single Responsibility Principle (SRP) — UML & Diagrams

---

## Class Diagram

```mermaid
classDiagram
    direction TB
    note for Client "See User, UserRepository"
    class Client {
        +main()
    }
    class Interface {
        <<abstract>>
    }
    class Concrete {
        +operation()
    }
    Client --> Interface
    Interface <|.. Concrete
```

---

## Sequence Diagram

```mermaid
sequenceDiagram
    actor User
    participant Client
    participant Service
    participant Impl
    User->>Client: trigger
    Client->>Service: call
    Service->>Impl: delegate
    Impl-->>User: result
```

---

## Object Relationship Diagram

```mermaid
graph TD
    Client --> Service
    Service --> ComponentA
    Service --> ComponentB
```

---

## ASCII Overview

```
+-------------+
|   Client    |
+------+------+
       |
       v
+-------------+
|  Abstraction |
+------+------+
       ^
       |
+-------------+
|  Concrete   |
+-------------+
```

---

## Activity Diagram

```mermaid
flowchart LR
    A([Start]) --> B[Initialize]
    B --> C[Execute]
    C --> D([End])
```

---

## 📌 Draw From Memory

Practice drawing: **Client → Abstraction → Concrete** with method labels.

