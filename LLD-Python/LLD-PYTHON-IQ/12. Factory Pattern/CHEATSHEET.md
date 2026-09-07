# Factory Pattern — Cheat Sheet

---

## One-Liner

> **Delegate object creation to a dedicated factory; clients use the product interface.**

---

## Intent

Encapsulate instantiation. Let subclasses or factory methods decide which class to instantiate.

---

## Participants

| Role | In This Repo |
|------|--------------|
| Product | `Food` (ABC) |
| Concrete Product | `Pizza`, `Burger`, `Pasta` |
| Creator / Factory | `FoodFactory` |
| Client | `RestrauntService` |

---

## When to Use ✅

- Object type determined at runtime
- Creation logic is complex or duplicated
- You want to hide concrete classes from clients
- Adding new types should not change client code

## When to Avoid ❌

- Single type, never changes
- Trivial `MyClass()` is enough

---

## Code Skeleton

```python
class Product(ABC):
    @abstractmethod
    def operation(self): ...

class Factory:
    @staticmethod
    def create(kind: str) -> Product:
        if kind == "a": return ConcreteA()
        if kind == "b": return ConcreteB()
```

---

## Pattern Comparisons

| | Factory | Abstract Factory | Builder |
|---|---------|------------------|---------|
| **Creates** | 1 product | Product family | Complex product |
| **Focus** | Which type | Which family | Which steps |

---

## SOLID Links

- **SRP** — Factory creates; Service uses
- **OCP** — Extend products, not clients
- **DIP** — Depend on `Food`, not `Pizza`

---

## Common Mistakes

- God factory with 50 if/elif branches
- No product interface (ABC)
- Confusing with Builder / Abstract Factory

---

## Real-World Examples

Zomato orders · Spring BeanFactory · Android LayoutInflater · Payment method selection

---

## 📌 5 Minute Revision

1. Problem: scattered creation
2. Solution: `FoodFactory.create_food()`
3. Client: `RestrauntService` only delegates
4. Benefit: OCP + testability
5. Next: Abstract Factory for product *families*

## 📌 1 Minute Revision

**Service asks Factory → Factory returns Product → prepare()**

## 📌 Related Patterns

Abstract Factory · Builder · Prototype · Simple Factory

## 📌 Next Topic

[13. Abstract Factory Pattern](../13.%20Abstract%20Factory%20Pattern/CHEATSHEET.md)
