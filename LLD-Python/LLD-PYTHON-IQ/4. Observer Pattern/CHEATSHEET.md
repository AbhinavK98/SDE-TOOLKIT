# Observer Pattern — Cheat Sheet

---

## One-Liner

> **Subject notifies all registered observers when state changes.**

---

## Participants

| Role | Class |
|------|-------|
| Subject | `WeatherStation` |
| Observer | `Observer` ABC |
| Concrete | `TVDisplay`, `MobileDisplay` |

---

## Key Methods

```
add_observer(obs)
remove_observer(obs)
update_temprature(temp)  → notify_observers()
observer.update(temp)
```

---

## When to Use ✅

- One object's state change affects many others
- You don't know how many dependents upfront
- MVC, event systems, live dashboards

## When to Avoid ❌

- Only one listener ever
- Observers need complex bidirectional sync

---

## vs Similar Patterns

| | Observer | Mediator | Strategy |
|---|----------|----------|----------|
| **Flow** | 1 → many notify | many ↔ hub | context → algorithm |
| **Intent** | React to state | Reduce coupling between peers | Swap behavior |

---

## Run

```bash
cd "4. Observer Pattern" && python main.py
```

---

## 📌 1 Minute Revision

**Subscribe → state change → loop observers → update(temp)**

## 📌 Next

[5. Strategy Pattern](../5.%20Strategy%20Pattern/CHEATSHEET.md)
