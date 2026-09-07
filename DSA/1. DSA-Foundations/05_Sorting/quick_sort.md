# Quick Sort

## Problem

Arrange array in non-decreasing order.

## Idea

Pick pivot, partition smaller left / larger right, recurse on sides.

## Visualization (ASCII)

```
pivot 5:  3 8 5 1 -> 3 1 |5| 8
```

## Dry Run

Pivot=5 on `[3,8,5,1]`: partition → `[3,1,5,8]`, recurse left `[3,1]`, right `[8]`.

## Brute Force Thinking

Try all permutations until sorted — O(n!) — teaches why we need smarter algorithms.

## Algorithm

Step-by-step in plain English before code.

## Python Code

```python
def quick_sort(arr, lo, hi):
    if lo >= hi:
        return
    p = partition(arr, lo, hi)
    quick_sort(arr, lo, p - 1)
    quick_sort(arr, p + 1, hi)

def partition(arr, lo, hi):
    pivot = arr[hi]
    i = lo
    for j in range(lo, hi):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[hi] = arr[hi], arr[i]
    return i
```

## Step-by-step Explanation

Walk through loops: what moves, what is invariant.

## Complexity

| Case | Time |
|------|------|
| Best | O(n log n) |
| Average | O(n log n) |
| Worst | O(n²) |
| Space | O(log n) stack |

## Properties

| Property | Value |
|----------|-------|
| Stable? | No |
| In-place? | Yes |
| Recursive? | Yes |
| Adaptive? | No |

## Best Use Cases

General in-memory sort; random pivot mitigates worst case.

## Comparison with other sorts

Faster average than merge in practice; worst case on sorted if bad pivot.

## Interview Questions

How to avoid O(n²)? Random pivot / median-of-three.

## Common Mistakes

Wrong pivot index; infinite recursion on partition bounds.

## Decision hint

See [comparison_table.md](comparison_table.md) and decision tree in [cheat_sheet.md](cheat_sheet.md).
