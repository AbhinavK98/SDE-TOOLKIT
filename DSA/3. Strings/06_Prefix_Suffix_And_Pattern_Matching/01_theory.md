# Prefix Suffix And Pattern Matching Pattern Theory

## Why this pattern matters

Naive matching restarts too much after a mismatch. KMP stores how much of the
current prefix is still useful. Z-algorithm stores match length from every index
against the prefix. Rolling hash compares substrings by numeric signatures.

## Recognition clues

- "find pattern"
- "prefix that is also suffix"
- "repeated substring"
- "shortest palindrome by adding in front"

## Common approaches

- Naive scan for small/simple constraints.
- KMP LPS table for deterministic O(n + m).
- Z-array for prefix match information.
- Rolling hash when many substring comparisons are needed.

## Important variations

- Exact substring search
- Detect periodic strings
- Palindrome prefix via combined string
- Matching across repeated boundaries

