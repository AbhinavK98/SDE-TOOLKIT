# Sorting Cheat Sheet

## 1-Minute

n log n comparison sorts: merge, quick, heap. Stable: merge, insertion, bubble.

## 5-Minute

- In-place: quick, heap, insertion
- Guaranteed O(n log n): merge, heap
- Adaptive: insertion, bubble
- Python: `list.sort()` in-place Timsort

## Common Mistakes

Confusing stability with correctness; bad pivot in quicksort.

## Pattern Recognition

| Need | Pick |
|------|------|
| Stable + guaranteed | Merge |
| In-place average fast | Quick |
| Top k elements | Heap, not full sort |
| Small n | Insertion |
