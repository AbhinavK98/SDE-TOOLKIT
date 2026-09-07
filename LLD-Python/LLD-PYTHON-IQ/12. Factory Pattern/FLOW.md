# Factory Pattern — Execution Flow

---

## Running the Good Example

```bash
cd "12. Factory Pattern"
python good_example.py
```

---

## Flowchart — `good_example.py`

```mermaid
flowchart TD
    Start([Module loads]) --> A[Create RestrauntService]
    A --> B[create_order 'pizza']
    B --> C[FoodFactory.create_food 'pizza']
    C --> D{food_type?}
    D -->|pizza| E[return Pizza]
    D -->|burger| F[return Burger]
    D -->|pasta| G[return Pasta]
    D -->|unknown| H[return None]
    E --> I[f.prepare]
    F --> I
    G --> I
    H --> J[Print 'Cannot prepare food']
    I --> K[Print 'Preparing ...']
    K --> L[create_order 'burger']
    L --> C
    L --> End([Done])
```

---

## Step-by-Step: First Order (`"pizza"`)

| Step | What Happens | Code Location |
|------|--------------|---------------|
| 1 | Python loads module | `good_example.py` top |
| 2 | `RestrauntService()` instantiated | line 54 |
| 3 | `create_order("pizza")` called | line 55 |
| 4 | Service calls `FoodFactory.create_food("pizza")` | line 46 |
| 5 | Factory matches `"pizza"` → `return Pizza()` | lines 34-35 |
| 6 | `f` is not `None` → `f.prepare()` | line 50 |
| 7 | `Pizza.prepare()` prints `"Preparing pizza"` | lines 17-18 |

---

## Step-by-Step: Second Order (`"burger"`)

Same flow; factory returns `Burger()`; prints `"Preparing burger"`.

---

## Bad Example Flow — Contrast

```mermaid
flowchart TD
    Start --> A[RestrauntService.create_order]
    A --> B{food_type inside service?}
    B -->|pizza| C[Pizza inside service]
    B -->|burger| D[Burger inside service]
    C --> E[prepare]
    D --> E
```

**Difference:** Creation `if/elif` lives **inside** `RestrauntService` — no separate factory.

---

## Object Call Sequence

```mermaid
sequenceDiagram
    autonumber
    participant M as Module
    participant RS as RestrauntService
    participant FF as FoodFactory
    participant P as Pizza

    M->>RS: RestrauntService()
    M->>RS: create_order("pizza")
    RS->>FF: create_food("pizza")
    FF->>P: __init__()
    P-->>FF: instance
    FF-->>RS: f
    RS->>P: prepare()
    P-->>M: stdout: Preparing pizza
```

---

## Decision Tree — When to Use Factory

```mermaid
flowchart TD
    Q1{Need to create objects?}
    Q1 -->|No| Done[No pattern needed]
    Q1 -->|Yes| Q2{Creation logic in multiple places?}
    Q2 -->|No| Q3{Will types grow over time?}
    Q2 -->|Yes| Factory[Use Factory Pattern]
    Q3 -->|Yes| Factory
    Q3 -->|No| Simple[Direct instantiation OK]
```

---

## Memory Flow

```
1. RestrauntService created on heap
2. create_order() pushed on call stack
3. FoodFactory.create_food() pushed on stack
4. Pizza() allocated on heap
5. Reference returned to create_order's local `f`
6. prepare() called — method lookup on Pizza class
7. Stack unwinds; `f` may be garbage collected if not returned
```

---

## 📌 Quick Revision

**Good:** `Service → Factory → Product → prepare()`  
**Bad:** `Service → if/elif create → prepare()`
