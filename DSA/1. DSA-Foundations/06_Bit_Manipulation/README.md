# Bit Manipulation

## What is it?

Using individual bits of integers to solve problems with XOR, AND, OR, shifts.

## Why do we need it?

O(1) operations on flags, parity, subsets, and certain optimizations.

## Real-world analogy

Light switches in a row — each bit is on/off; XOR toggles, AND masks.

## Visualization

```
5 = 101, 3 = 011, 5&3 = 001 = 1
```

## Where interviewers ask it

Single number, power of two, subset bitmask, counting bits.

## Advantages

- Extremely fast
- Compact state representation

## Disadvantages

- Harder to read
- Limited problem class

## When NOT to use it

When clarity matters more than micro-optimization on large structures.

## Interview Tricks

- n & (n-1) clears lowest set bit
- n & -n gets lowest set bit

## Cheat Sheet

See [Cheat Sheet](cheat_sheet.md)

## Revision Notes

- **5 min**: Read section headers + one dry run.
- **1 min**: Recall WHY / HOW / WHEN / WHAT for this topic.
- **Before interview**: Skim cheat sheet + common mistakes.

## Files in this section

- [theory.md](theory.md)
- [operations.md](operations.md)
- [patterns.md](patterns.md)
- [cheat_sheet.md](cheat_sheet.md)
- [practice_questions.md](practice_questions.md)
