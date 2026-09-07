# Heap Sort

## Problem

Arrange array in non-decreasing order.

## Idea

Build max-heap, repeatedly extract max to end.

## Visualization (ASCII)

```
Max heap tree:
    10
   /  \
  4    3
```

## Dry Run

Build heap on `[4,10,3]`, swap max to end, heapify reduced heap.

## Brute Force Thinking

Try all permutations until sorted — O(n!) — teaches why we need smarter algorithms.

## Algorithm

Step-by-step in plain English before code.

## Python Code

```python
def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for end in range(n - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        heapify(arr, end, 0)

def heapify(arr, n, i):
    largest = i
    l, r = 2 * i + 1, 2 * i + 2
    if l < n and arr[l] > arr[largest]: largest = l
    if r < n and arr[r] > arr[largest]: largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
```

## Step-by-step Explanation

Walk through loops: what moves, what is invariant.

## Complexity

| Case | Time |
|------|------|
| Best | O(n log n) |
| Average | O(n log n) |
| Worst | O(n log n) |
| Space | O(1) |

## Properties

| Property | Value |
|----------|-------|
| Stable? | No |
| In-place? | Yes |
| Recursive? | Can be |
| Adaptive? | No |

## Best Use Cases

When guaranteed O(n log n) in-place needed.

## Comparison with other sorts

O(1) extra space vs merge; not stable; slower constants than quick.

## Interview Questions

Relation to priority queue / heap data structure.

## Common Mistakes

Heapify wrong range after shrink.

## Decision hint

See [comparison_table.md](comparison_table.md) and decision tree in [cheat_sheet.md](cheat_sheet.md).
