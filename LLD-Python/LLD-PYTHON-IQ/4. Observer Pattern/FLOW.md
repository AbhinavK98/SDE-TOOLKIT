# Observer Pattern — Execution Flow

---

## How to Run

```bash
cd "4. Observer Pattern"
python main.py
```

---

## Full Execution Flowchart

```mermaid
flowchart TD
    Start([python main.py]) --> A[WeatherStation created]
    A --> B[TVDisplay created]
    B --> C[add_observer TV]
    C --> D[update_temprature 30]
    D --> E[notify_observers]
    E --> F[TV.update 30]
    F --> G[MobileDisplay created]
    G --> H[add_observer Mobile]
    H --> I[update_temprature 35]
    I --> J[notify: TV + Mobile]
    J --> K[remove_observer TV]
    K --> L[update_temprature 40]
    L --> M[notify: Mobile only]
    M --> End([Done])
```

---

## Step-by-Step Trace

### Phase 1 — TV Only (temp = 30)

| Step | Code | Output |
|------|------|--------|
| 1 | `ws = WeatherStation()` | Empty observer list |
| 2 | `tv = TVDisplay()` | TV observer created |
| 3 | `ws.add_observer(tv)` | `[tv]` in list |
| 4 | `ws.update_temprature(30)` | Sets `__temprature=30`, calls notify |
| 5 | `tv.update(30)` | `TV Display: Temperature updated to 30°C` |

### Phase 2 — TV + Mobile (temp = 35)

| Step | Code | Effect |
|------|------|--------|
| 6 | `mobile = MobileDisplay()` | New observer |
| 7 | `ws.add_observer(mobile)` | `[tv, mobile]` |
| 8 | `ws.update_temprature(35)` | Both `update(35)` called |

### Phase 3 — Mobile Only (temp = 40)

| Step | Code | Effect |
|------|------|--------|
| 9 | `ws.remove_observer(tv)` | `[mobile]` |
| 10 | `ws.update_temprature(40)` | Only mobile notified |

---

## Inside `notify_observers()`

```mermaid
flowchart LR
    A[notify_observers] --> B{For each observer}
    B --> C[observer.update __temprature]
    C --> B
    B -->|done| D[return]
```

```python
def notify_observers(self):
    for observer in self.__observers:
        observer.update(self.__temprature)
```

---

## Sequence Diagram (Complete Run)

```mermaid
sequenceDiagram
    autonumber
    participant M as main.py
    participant WS as WeatherStation
    participant TV as TVDisplay
    participant MO as MobileDisplay

    M->>WS: WeatherStation()
    M->>TV: TVDisplay()
    M->>WS: add_observer(tv)
    M->>WS: update_temprature(30)
    WS->>TV: update(30)

    M->>MO: MobileDisplay()
    M->>WS: add_observer(mobile)
    M->>WS: update_temprature(35)
    WS->>TV: update(35)
    WS->>MO: update(35)

    M->>WS: remove_observer(tv)
    M->>WS: update_temprature(40)
    WS->>MO: update(40)
```

---

## Push vs Pull Models

This repo uses **push** — subject sends `temp` to observers.

```mermaid
flowchart TD
    subgraph Push["Push (this repo)"]
        S1[Subject] -->|update temp| O1[Observer]
    end
    subgraph Pull["Pull (alternative)"]
        S2[Subject] -->|notify only| O2[Observer]
        O2 -->|observer.get_state| S2
    end
```

---

## Memory During Execution

After step 7 (`add_observer(mobile)`):

```
WeatherStation.__observers
    [0] ──► TVDisplay instance
    [1] ──► MobileDisplay instance
```

After step 9 (`remove_observer(tv)`):

```
WeatherStation.__observers
    [0] ──► MobileDisplay instance
```

---

## 📌 Quick Revision

**Subscribe → Change state → Notify all → Unsubscribe → Notify remaining**
