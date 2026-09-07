# Bit Manipulation Theory

## WHAT

Computers store integers in binary. Bit operations work on those 0/1 positions directly.

## WHY

Some problems have symmetries (XOR cancellation) or need compact sets (bitmask DP).

## Binary refresher

```
5 decimal = 101 binary
3 decimal = 011 binary
```

## Core operations

| Op | Meaning | Example |
|----|---------|---------|
| & | AND | both 1 → 1 |
| \| | OR | either 1 → 1 |
| ^ | XOR | different → 1 |
| << | left shift | multiply by 2^k |
| >> | right shift | divide by 2^k |

## XOR properties (WHY many problems work)

- a ^ a = 0
- a ^ 0 = a
- Commutative & associative

**Use case:** Find single number when all others appear twice.

## Common Mistakes

- Confusing logical vs bitwise operators
- Sign issues with right shift on negative numbers in some languages

See [operations.md](operations.md), [patterns.md](patterns.md).
