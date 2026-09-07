# Binary Search

## WHAT
Repeatedly halve search space in **sorted** array.

## WHY O(log n)
Each step eliminates half → at most log₂(n) steps.

## Visualization

```
Indices: 0  1  2  3  4  5  6  7
Values:  1  3  5  7  9 11 13 15
                 ↑ mid=7, target 9 > 7 → go right
```

## Template (inclusive bounds)

```python
def binary_search(arr: list[int], target: int) -> int:
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2  # avoid overflow in other langs
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
```

## Dry Run

`[1,3,5,7,9]`, target=5: mid=2, arr[2]=5 → return 2

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| `mid = (lo+hi)/2` overflow | Use `lo + (hi-lo)//2` |
| Infinite loop | Update lo/hi correctly |
| Wrong loop condition | `lo <= hi` for inclusive |

## Complexity

Time O(log n), Space O(1)
