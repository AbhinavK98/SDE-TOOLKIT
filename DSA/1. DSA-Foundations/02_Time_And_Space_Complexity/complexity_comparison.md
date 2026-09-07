# Complexity Comparison — Data Structures

## Operations (Average Case)

| Structure | Access | Search | Insert | Delete | Space |
|-----------|--------|--------|--------|--------|-------|
| Array | O(1) | O(n) | O(n) | O(n) | O(n) |
| Linked List | O(n) | O(n) | O(1)* | O(1)* | O(n) |
| Stack | O(n) | O(n) | O(1) | O(1) | O(n) |
| Queue | O(n) | O(n) | O(1) | O(1) | O(n) |
| HashMap | — | O(1) | O(1) | O(1) | O(n) |
| BST (balanced) | O(log n) | O(log n) | O(log n) | O(log n) | O(n) |
| Heap | — | O(n) | O(log n) | O(log n) | O(n) |

*At known position

---

## Sorting Comparison

| Algorithm | Best | Average | Worst | Space | Stable |
|-----------|------|---------|-------|-------|--------|
| Bubble | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Selection | O(n²) | O(n²) | O(n²) | O(1) | No |
| Insertion | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Merge | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |
| Quick | O(n log n) | O(n log n) | O(n²) | O(log n) | No |
| Heap | O(n log n) | O(n log n) | O(n log n) | O(1) | No |

See [../05_Sorting/comparison_table.md](../05_Sorting/comparison_table.md).

---

## Searching Comparison

| Method | Precondition | Time |
|--------|--------------|------|
| Linear | None | O(n) |
| Binary | Sorted | O(log n) |
| Hash lookup | Hashable keys | O(1) avg |

---

## Trees and Graphs

| Traversal | Time | Space (stack/queue) |
|-----------|------|---------------------|
| DFS | O(V+E) | O(V) |
| BFS | O(V+E) | O(V) |
| BST search | O(h) height | O(1) iterative |

---

## WHEN to choose what

- Need fast lookup by key → HashMap
- Need order + range queries → BST / sorted array + BS
- Need min/max repeatedly → Heap
- Need FIFO → Queue
- Need LIFO / undo → Stack
