# Selection Sort

## Problem

Arrange array in non-decreasing order.

## Idea

Find minimum of unsorted portion, swap to front. Sorted region grows left to right.

## Visualization (ASCII)

```
[ unsorted | sorted growing ]
  pick min -> swap to front
```

## Dry Run

`[64,25,12,22]`: i=0 min=12 swap→`[12,25,64,22]`; i=1 min=22→`[12,22,64,25]`...

## Brute Force Thinking

Try all permutations until sorted — O(n!) — teaches why we need smarter algorithms.

## Algorithm

Step-by-step in plain English before code.

## Python Code

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
```

## Step-by-step Explanation

Walk through loops: what moves, what is invariant.

## Complexity

| Case | Time |
|------|------|
| Best | O(n²) |
| Average | O(n²) |
| Worst | O(n²) |
| Space | O(1) |

## Properties

| Property | Value |
|----------|-------|
| Stable? | No (swap can jump equal elements) |
| In-place? | Yes |
| Recursive? | Optional |
| Adaptive? | No |

## Best Use Cases

When memory writes are expensive (theoretical).

## Comparison with other sorts

Fewer swaps than bubble but always n² comparisons.

## Interview Questions

Why not stable? Long-distance swap.

## Common Mistakes

Updating min_idx; off-by-one in inner loop start.

## Decision hint

See [comparison_table.md](comparison_table.md) and decision tree in [cheat_sheet.md](cheat_sheet.md).
