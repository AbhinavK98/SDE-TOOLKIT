# Greedy And Sorting Strings Pattern Cheatsheet

## Pattern Comparison

| Variant | Core idea |
|---|---|
| Partition labels | close segment at farthest last index |
| Remove K digits | monotonic increasing stack |
| Reorganize string | max heap by remaining count |
| Largest number | custom concatenation comparator |
| Custom sort | count then emit in requested order |

## Common complexities

- Sorting characters: O(n log n)
- Counting fixed alphabet: O(n)
- Heap construction: O(n log a), where a is distinct characters

