# Liskov Substitution Principle (LSP) — Cheat Sheet

---

## One-Liner

> Subclass breaks parent contract — `FixedDepositAccount.withdraw()` raises Exception. Code expecting ...

---

## Intent

Solve **Liskov Substitution Principle (LSP)** problems through structured object collaboration.

---

## Key Classes

`Account, WithdrawableAccount, SavingsAccount, FixedDepositAccount`

---

## When to Use ✅

- System must grow without breaking existing code
- Multiple implementations of same behavior
- Clear interview LLD scenario matches this pattern

## When to Avoid ❌

- Single class, no variation, no growth expected

---

## Run Command

```bash
cd '2. Good Example' && python main.py
```

---

## SOLID Links

| Principle | Connection |
|-----------|------------|
| SRP | One class, one job |
| OCP | Extend, don't modify |
| DIP | Depend on abstractions |

---

## Common Mistakes

- Over-engineering
- Wrong pattern for the problem
- Can't draw UML from memory

---

## 📌 5 Minute Revision

1. Problem: Subclass breaks parent contract — `FixedDepositAccount.withdraw()` raises Except...
2. Analogy: Every **bird** should fly. If **Penguin** extends Bird but can't fly, the abstra...
3. Run the code
4. Draw class diagram
5. Explain bad vs good

## 📌 1 Minute Revision

**main → FixedDepositAccount.deposit(1000)**

## 📌 Next Topic

**Interface Segregation Principle (ISP)**

