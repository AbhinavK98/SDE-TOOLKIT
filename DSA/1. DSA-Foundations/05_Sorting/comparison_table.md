# Sorting Comparison Table

| Algorithm | Best | Avg | Worst | Space | Stable | In-place |
|-----------|------|-----|-------|-------|--------|----------|
| Bubble | O(n) | O(n²) | O(n²) | O(1) | Yes | Yes |
| Selection | O(n²) | O(n²) | O(n²) | O(1) | No | Yes |
| Insertion | O(n) | O(n²) | O(n²) | O(1) | Yes | Yes |
| Merge | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes | No |
| Quick | O(n log n) | O(n log n) | O(n²) | O(log n) | No | Yes |
| Heap | O(n log n) | O(n log n) | O(n log n) | O(1) | No | Yes |

## Decision Tree: When should I use this sorting algorithm?

```
Need stable sort?
├── Yes -> Merge sort (or insertion for tiny n)
└── No -> Need worst-case O(n log n) guaranteed?
          ├── Yes -> Heap sort or Merge sort
          └── No -> Quick sort (average fast)
                    └── Nearly sorted small? -> Insertion sort
```

## Interview comparison questions

- Merge vs Quick: stability, space, worst case
- When is O(n²) acceptable? n very small
- Python `sorted()` uses Timsort — hybrid stable O(n log n)
