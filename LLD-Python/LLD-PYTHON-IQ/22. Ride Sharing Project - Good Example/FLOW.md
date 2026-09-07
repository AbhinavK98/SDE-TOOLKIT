# Ride Sharing Good Example — Execution Flow

---

## Run

```bash
cd "22. Ride Sharing Project - Good Example"
python client.py
```

---

## End-to-End Flowchart

```mermaid
flowchart TD
    Start([client.py]) --> L1[Create Locations loc1 loc2 loc3]
    L1 --> V1[Create Car CS9999]
    V1 --> D1[Create Driver Alice with car at loc2]
    D1 --> P1[Create Passenger Anirudh at loc2]
    P1 --> RMS[Create RideMatchingService]
    RMS --> AD[add_driver driver1]
    AD --> RR[requestRide passenger 50 LuxuryFareStrategy]
    RR --> CHK{Drivers available?}
    CHK -->|No| NF[notify No Drivers]
    CHK -->|Yes| FIND[__findNearestDriver]
    FIND --> REM[Remove driver from pool]
    REM --> CR[Create Ride]
    CR --> CF[calculateFare]
    CF --> N1[Notify passenger + driver]
    N1 --> ON[updateStatus ONGOING]
    ON --> CMP[updateStatus COMPLETED]
    CMP --> RET[Return driver to pool]
    RET --> End([Done])
```

---

## Fare Calculation Detail

```
Car.get_fare_amount()     = 20
distance                  = 50
LuxuryFareStrategy        = × 1.5

fare = 20 × 50 × 1.5 = Rs. 1500
```

```mermaid
flowchart LR
    V[Vehicle.get_fare_amount] --> M[× distance]
    M --> S[× strategy multiplier]
    S --> F[Final fare]
```

---

## Nearest Driver Algorithm

```python
for driver in __available_drivers:
    dist = driver.get_location().calcDistance(passenger_location)
    if dist < minDistance:
        assignedDriver = driver
```

With one driver in `client.py`, Alice is always selected.

---

## Ride Status State Machine

```mermaid
stateDiagram-v2
    [*] --> SCHEDULED: Ride created
    SCHEDULED --> ONGOING: updateStatus ONGOING
    ONGOING --> COMPLETED: updateStatus COMPLETED
    COMPLETED --> [*]
```

Each transition calls `__notifyUsers()` — passenger and driver both notified.

---

## Sequence Diagram

```mermaid
sequenceDiagram
    participant Client
    participant RMS as RideMatchingService
    participant Ride
    participant P as Passenger
    participant D as Driver
    participant FS as LuxuryFareStrategy

    Client->>RMS: add_driver(Alice)
    Client->>RMS: requestRide(Anirudh, 50, Luxury)
    RMS->>RMS: findNearestDriver()
    RMS->>Ride: new Ride(...)
    Ride->>FS: calFare(car, 50)
    Ride->>P: notify(scheduled message)
    Ride->>D: notify(new ride message)
    Ride->>Ride: ONGOING → notify both
    Ride->>Ride: COMPLETED → notify both
    RMS->>RMS: add_driver(Alice) back
```

---

## 📌 Quick Revision

**Match → Fare (Strategy) → Notify → ONGOING → COMPLETED → Return driver**
