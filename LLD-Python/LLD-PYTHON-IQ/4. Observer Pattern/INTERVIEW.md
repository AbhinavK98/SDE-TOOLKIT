# Observer Pattern — Interview Q&A

---

### 1. What is the Observer Pattern?

**Answer:** A behavioral pattern defining a one-to-many dependency between objects. When a subject's state changes, all registered observers are automatically notified and updated. The subject doesn't need to know concrete observer classes.

---

### 2. Who are the participants in this repo's example?

| Role | Class |
|------|-------|
| Subject | `WeatherStation` |
| Observer (interface) | `Observer` |
| Concrete Observers | `TVDisplay`, `MobileDisplay` |
| Client | `main.py` |

---

### 3. Difference between Observer and Pub/Sub?

| Observer | Pub/Sub |
|----------|---------|
| Subject knows observers directly | Broker sits between publisher and subscribers |
| In-process, synchronous typically | Often async, distributed (Kafka, RabbitMQ) |
| `add_observer()` | `subscribe(topic)` |

---

### 4. Difference between Observer and Mediator?

| Observer | Mediator |
|----------|----------|
| Subject broadcasts to many observers | Colleagues communicate only through mediator |
| One-to-many | Many-to-many via hub |
| This repo: folder 4 | This repo: folder 10 |

---

### 5. Push vs Pull model?

**Push (this repo):** Subject sends data: `observer.update(self.__temprature)`  
**Pull:** Subject only signals change; observer calls `subject.get_temperature()`

Push is simpler; pull reduces unnecessary data transfer when observers need different fields.

---

### 6. How does Observer relate to MVC?

**Model** = Subject. **View** = Observer. Model changes → views update. Controller handles user input separately.

---

### 7. What happens if you forget `remove_observer`?

The observer stays in the list — memory leak and stale updates to destroyed UI components. Always unsubscribe in destructors/cleanup.

---

### 8. How would you implement thread-safe Observer?

Use a copy of the observer list during notification, or lock the list while iterating. Python's GIL helps but async systems need care.

---

### 9. Design a stock price notification system.

`StockExchange` (subject) with `add_investor()`. `Investor` (observer) implements `update(price)`. On trade, `notify_all(price)`.

---

### 10. Can Observer cause infinite loops?

Yes — if observer A changes subject state which notifies B which changes subject again. Guard with change flags or event debouncing.

---

### 11. Python `@property` vs Observer?

`@property` notifies on attribute access/set within one object. Observer is **cross-object** notification.

---

### 12. Is `notify()` in Ride Sharing (folder 22) Observer Pattern?

It's **observer-like** — users get notified on ride events. Full Observer would have a subject maintaining an observer list. The *intent* (react to changes) is the same.

---

### 13. Advantages in interviews?

Loose coupling, OCP (new observers without editing subject), dynamic subscription, supports event-driven architecture.

---

### 14. Disadvantages?

Unexpected update order, debugging complexity, risk of memory leaks, potential performance hit with many observers.

---

### 15. Whiteboard: draw Observer for a news agency.

`NewsAgency` publishes article → `Subscriber` (email), `Subscriber` (SMS), `Subscriber` (app push) all implement `update(article)`.

---

## 📌 Interview Tip

> Start with the **problem** (tight coupling when adding displays), then introduce Subject + Observer interface.
