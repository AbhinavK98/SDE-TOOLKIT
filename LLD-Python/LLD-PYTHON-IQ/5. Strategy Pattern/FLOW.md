# Strategy Pattern — Execution Flow

---

## How to Run

```bash
cd "5. Strategy Pattern"
python main.py
```

---

## Flowchart

```mermaid
flowchart TD
    Start([Program Start]) --> Load[Load modules / classes]
    Load --> Init[Initialize objects]
    Init --> Action[Main action / demo]
    Action --> Delegate{Delegate to collaborators?}
    Delegate -->|Yes| Sub[Component executes]
    Delegate -->|No| Direct[Direct method call]
    Sub --> Output[Print / return result]
    Direct --> Output
    Output --> End([End])
```

---

## Step-by-Step

| Step | Action |
|------|--------|
| 1 | Python interpreter loads `.py` files |
| 2 | Classes defined on heap (type objects) |
| 3 | Module-level or main code creates instances |
| 4 | DiscountService(DiwaliStrategy) → process → set_strategy(Holi) → process |
| 5 | Output printed to stdout |

---

## Sequence Diagram

```mermaid
sequenceDiagram
    autonumber
    participant Main
    participant A as Primary Class
    participant B as Collaborator
    Main->>A: create / call
    A->>B: delegate
    B-->>A: result
    A-->>Main: output
```

---

## Decision Tree

```mermaid
flowchart TD
    Q{Need this pattern?}
    Q -->|Problem matches| Yes[Apply pattern]
    Q -->|Trivial problem| No[Keep it simple]
```

---

## 📌 Quick Revision

**Flow:** DiscountService(DiwaliStrategy) → process → set_strategy(Holi) → process

