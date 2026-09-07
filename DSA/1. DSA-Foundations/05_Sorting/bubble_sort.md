# Bubble Sort

## Problem

Arrange array in non-decreasing order.

## Idea

Repeatedly swap adjacent elements if out of order. Largest 'bubbles' to end each pass.

## Visualization (ASCII)

```
Pass 1: 5 4 2 1 -> 4 2 1 |5|
Pass 2: 4 2 1 5 -> 2 1 |4| 5
```

## Dry Run

`[5,4,2,1]`: Pass1 swaps → `[4,2,1,5]`; Pass2 → `[2,1,4,5]`; Pass3 → `[1,2,4,5]`.

## Brute Force Thinking

Try all permutations until sorted — O(n!) — teaches why we need smarter algorithms.

## Algorithm

Step-by-step in plain English before code.

## Python Code

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
```

## Step-by-step Explanation

Walk through loops: what moves, what is invariant.

## Complexity

| Case | Time |
|------|------|
| Best | O(n) |
| Average | O(n²) |
| Worst | O(n²) |
| Space | O(1) |

## Properties

| Property | Value |
|----------|-------|
| Stable? | Yes |
| In-place? | Yes |
| Recursive? | No |
| Adaptive? | Yes (with early exit) |

## Best Use Cases

Teaching; nearly sorted tiny arrays with adaptive optimization.

## Comparison with other sorts

Slower than merge/quick; only educational or tiny n.

## Interview Questions

Why O(n) best case? No swaps → one pass.

## Common Mistakes

Wrong inner loop bound `n-i-1`; forgetting early exit optimization.

## Decision hint

See [comparison_table.md](comparison_table.md) and decision tree in [cheat_sheet.md](cheat_sheet.md).
