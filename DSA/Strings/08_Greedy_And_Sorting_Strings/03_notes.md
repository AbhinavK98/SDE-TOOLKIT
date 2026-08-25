# Greedy And Sorting Strings Pattern Notes

## Revision in 5 minutes

- Partition labels -> current segment must reach farthest last occurrence.
- Remove K digits -> pop larger previous digits while you can.
- Reorganize -> repeatedly use the most frequent non-blocked character.
- Largest number -> compare `a+b` vs `b+a`.
- Unique frequencies -> decrement duplicates until unused.

## Common mistakes

- Not removing leftover digits when number is already increasing.
- Returning leading zeroes in Remove K Digits.
- Sorting numbers numerically for Largest Number.
- Reusing the same char immediately in Reorganize String.

## Revision in 1 minute

- Need best construction -> find the local choice and its invariant.

