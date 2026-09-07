# Merge Sort

## Problem

Arrange array in non-decreasing order.

## Idea

Divide array in half, sort each half recursively, merge two sorted halves.

## Visualization (ASCII)

```
       [38 27 43 3]
      /            \
  [38 27]        [43 3]
   /   \          /   \
[38][27]      [43] [3]
   merge up
```

## Dry Run

`[38,27,43,3]`: split → `[38,27]` `[43,3]` → sort → `[27,38]` `[3,43]` → merge → `[3,27,38,43]`.

## Brute Force Thinking

Try all permutations until sorted — O(n!) — teaches why we need smarter algorithms.

## Algorithm

Step-by-step in plain English before code.

## Python Code

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:]); result.extend(right[j:])
    return result
```

## Step-by-step Explanation

Walk through loops: what moves, what is invariant.

## Complexity

| Case | Time |
|------|------|
| Best | O(n log n) |
| Average | O(n log n) |
| Worst | O(n log n) |
| Space | O(n) |

## Properties

| Property | Value |
|----------|-------|
| Stable? | Yes |
| In-place? | No (typical) |
| Recursive? | Yes |
| Adaptive? | No |

## Best Use Cases

Linked list sort, external sort, stable sort needed.

## Comparison with other sorts

Guaranteed O(n log n); extra space vs quicksort.

## Interview Questions

Draw recursion tree; n log n levels × n merge.

## Common Mistakes

Forgetting remaining elements after merge loop.

## Decision hint

See [comparison_table.md](comparison_table.md) and decision tree in [cheat_sheet.md](cheat_sheet.md).
