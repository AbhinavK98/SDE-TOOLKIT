# Insertion Sort

## Problem

Arrange array in non-decreasing order.

## Idea

Build sorted prefix; insert each new element into correct position by shifting.

## Visualization (ASCII)

```
|2 5 8| 3  -> shift -> |2 5|3 8 -> |2 3 5| 8
```

## Dry Run

`[5,2,4]`: i=1 key=2 shift 5→`[5,5,4]` insert 2→`[2,5,4]`; i=2 key=4→`[2,4,5]`.

## Brute Force Thinking

Try all permutations until sorted — O(n!) — teaches why we need smarter algorithms.

## Algorithm

Step-by-step in plain English before code.

## Python Code

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
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
| Recursive? | Yes |
| Adaptive? | Yes |

## Best Use Cases

Small n, online sorting (stream), hybrid sort sub-routine.

## Comparison with other sorts

Better than bubble/selection on small/nearly sorted data.

## Interview Questions

Used inside Timsort for small runs.

## Common Mistakes

Shifting wrong direction; j goes negative check.

## Decision hint

See [comparison_table.md](comparison_table.md) and decision tree in [cheat_sheet.md](cheat_sheet.md).
