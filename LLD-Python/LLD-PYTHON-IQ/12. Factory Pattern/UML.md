# Factory Pattern — UML & Diagrams

---

## Class Diagram (Good Example)

```mermaid
classDiagram
    direction TB
    class Food {
        <<abstract>>
        +prepare()*
    }
    class Pizza {
        +prepare()
    }
    class Burger {
        +prepare()
    }
    class Pasta {
        +prepare()
    }
    class FoodFactory {
        +create_food(type) Food$
    }
    class RestrauntService {
        +create_order(type)
    }
    Food <|.. Pizza : implements
    Food <|.. Burger : implements
    Food <|.. Pasta : implements
    RestrauntService --> FoodFactory : uses
    FoodFactory ..> Pizza : creates
    FoodFactory ..> Burger : creates
    FoodFactory ..> Pasta : creates
    RestrauntService --> Food : uses
```

---

## Class Diagram (Bad Example)

```mermaid
classDiagram
    class Food {
        <<abstract>>
        +prepare()*
    }
    class Pizza
    class Burger
    class RestrauntService {
        +create_order(type)
    }
    Food <|-- Pizza
    Food <|-- Burger
    RestrauntService ..> Pizza : creates directly
    RestrauntService ..> Burger : creates directly
```

---

## Sequence Diagram

```mermaid
sequenceDiagram
    actor Client
    participant RS as RestrauntService
    participant FF as FoodFactory
    participant Product as Food

    Client->>RS: create_order("pizza")
    RS->>FF: create_food("pizza")
    FF->>Product: new Pizza()
    Product-->>FF: instance
    FF-->>RS: Food reference
    RS->>Product: prepare()
    Product-->>Client: output
```

---

## Activity Diagram

```mermaid
flowchart LR
    A([Start]) --> B[Receive food_type]
    B --> C[Delegate to Factory]
    C --> D{Valid type?}
    D -->|Yes| E[Instantiate product]
    D -->|No| F[Handle error]
    E --> G[Call prepare]
    G --> H([End])
    F --> H
```

---

## Object Relationship Diagram

```mermaid
graph TD
    subgraph Client Layer
        RS[RestrauntService]
    end
    subgraph Creation Layer
        FF[FoodFactory]
    end
    subgraph Product Layer
        P[Pizza]
        B[Burger]
        PA[Pasta]
    end
    RS -->|depends on| FF
    RS -->|uses| P
    FF -->|creates| P
    FF -->|creates| B
    FF -->|creates| PA
```

---

## ASCII Class Diagram

```
+---------------------+
|  RestrauntService   |
+---------------------+
| + create_order()    |
+----------+----------+
           | uses
           v
+---------------------+
|    FoodFactory      |
+---------------------+
| + create_food() $   |
+----------+----------+
           | creates
     +-----+-----+
     v           v
+--------+   +--------+
| Pizza  |   | Burger |
+--------+   +--------+
     ^           ^
     |           |
     +-----+-----+
           |
    implements Food.prepare()
```

---

## State: Object Graph at Runtime

After `create_order("pizza")`:

```mermaid
graph LR
    RS[RestrauntService] -.->|local var f| P[Pizza instance]
    P -->|class| PC[Pizza class]
    PC -->|inherits| FC[Food ABC]
```

---

## Comparison: Factory vs Related Patterns

```mermaid
graph TD
    FP[Factory Pattern]
    AFP[Abstract Factory]
    BP[Builder]
    PP[Prototype]
    FP -->|one product| P1[Pizza]
    AFP -->|product family| P2[Starter + Main + Dessert]
    BP -->|step by step| P3[Laptop with 5 options]
    PP -->|clone| P4[Copy ChessBoard]
```

---

## 📌 Diagram Revision

Draw from memory: **Client → Factory → Product**. Factory has `create()`; Product has shared interface.
