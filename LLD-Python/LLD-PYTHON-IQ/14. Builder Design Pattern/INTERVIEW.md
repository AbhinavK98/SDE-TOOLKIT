# Builder Pattern — Interview Q&A

---

## Core Questions

### 1. What problem does Builder Pattern solve?

**Answer:** Laptop with 5 optional params needs telescoping constructors: Laptop(cpu, ram, None, None, screen).

---

### 2. Explain the real-world analogy.

**Answer:** **Custom Starbucks drink** — size, milk, shots, syrup — built step by step, not one giant constructor.

---

### 3. Walk through the code in this folder.

**Answer:** Key classes: `Laptop, LaptopBuilder`. Flow: LaptopBuilder().set_processor().set_ram().build().

---

### 4. What are the advantages?

- Extensibility without modifying existing code
- Clear separation of responsibilities
- Easier unit testing with mocked dependencies
- Better alignment with SOLID principles

---

### 5. What are the disadvantages?

- Additional classes and indirection
- Risk of over-engineering simple problems
- Steeper onboarding for new team members

---

### 6. Bad vs Good — what's the difference?

| Bad | Good |
|-----|------|
| Laptop(cpu, ram, gpu, color, screen) with many Nones | LaptopBuilder fluent setters → build() |

---

### 7. How does this relate to SOLID?

- **SRP:** Each class has one reason to change
- **OCP:** Extend via new classes, not edits
- **LSP:** Subtypes honor parent contracts
- **ISP:** Small, focused interfaces
- **DIP:** Depend on abstractions

---

### 8. Where would you use this in production?

**Sample answer:** "In our notification pipeline / payment service / ride matching system, we applied this to [specific problem], which let us add [feature] without touching [existing code]."

---

### 9. How would you test this design?

- Unit test each class in isolation
- Mock collaborators via interfaces
- Integration test the orchestration layer (main/client)

---

### 10. When should you NOT use this pattern?

When the problem is trivial, unlikely to change, and a simple function or class suffices.

---

### 11. Design a system using this pattern (whiteboard).

Draw: Client → Abstraction → Concrete. Label method calls. Mention extensibility.

---

### 12. Compare with a similar pattern.

See CHEATSHEET.md comparison table and NOTES.md.

---

### 13. What Python features are used?

`abc.ABC`, `@abstractmethod`, type hints, encapsulation with `__`, composition, and sometimes `Enum` or `copy.deepcopy`.

---

### 14. Common mistakes interviewers flag?

God classes, wrong pattern choice, unable to draw diagram, confusing similar patterns.

---

### 15. One-minute elevator pitch?

> **Laptop with 5 optional params needs telescoping constructors: Laptop(cpu, ram, None, None, screen)....** This folder shows the fix.

---

## 📌 Interview Tip

> Always: **Requirements → Problems → Pattern → Classes → Walkthrough**

