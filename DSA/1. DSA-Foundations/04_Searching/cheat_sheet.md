# Searching Cheat Sheet

## 1-Minute

Sorted → binary search O(log n). Unsorted → linear O(n) or hash O(1).

## 5-Minute

- Inclusive: `while lo <= hi`
- Exclusive hi: `while lo < hi`, hi = len(arr)
- BS on answer needs monotonic predicate

## Pattern Recognition

| Clue | Technique |
|------|-----------|
| Sorted array | Binary search |
| Minimize maximum | BS on answer |
| Rotated sorted | BS with sorted half check |
| First/last position | Lower/upper bound |

## Common Mistakes

Off-by-one, wrong mid update, forgetting empty input.
