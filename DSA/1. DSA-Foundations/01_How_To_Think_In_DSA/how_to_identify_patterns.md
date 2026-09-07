# How To Identify Patterns

Patterns are **reusable solution shapes**. Recognition saves minutes in interviews.

---

## Pattern Recognition Table

| You hear / see | Pattern | Foundation topic |
|----------------|---------|------------------|
| Pair, complement, duplicate | HashMap | Arrays HashMap |
| Sorted + pair sum | Two pointers | Searching |
| Subarray sum, window | Sliding window / Prefix | Arrays |
| All combinations | Backtracking | Recursion |
| Sorted search | Binary search | Searching |
| Tree / graph traversal | DFS / BFS | Recursion |
| Optimal substructure | DP | Recursion + Math |
| Bits, XOR, powers of 2 | Bit manipulation | Bit Manipulation |

---

## HOW to practice recognition

1. Solve problem brute force.
2. Label the bottleneck (nested loop? repeated sum?).
3. Match bottleneck to pattern from table.
4. After 50 problems, recognition becomes automatic.

---

## WHEN pattern recognition fails

- Problem is ad-hoc simulation
- Greedy proof is non-obvious
- **Action:** Stick to brute force + small optimizations; do not force a pattern.

---

## Decision Tree (ASCII)

```
Is input sorted?
├── Yes -> Two pointers or Binary Search?
│         ├── Need index in original -> HashMap or modified BS
│         └── In-place -> Two pointers
└── No -> Need fast lookup?
          ├── Yes -> HashMap
          └── Contiguous subarray?
                ├── Fixed size -> Sliding window
                └── Variable size -> Expand/shrink window
```

---

## Common Mistakes

- Forcing DP on every problem
- Using binary search on unsorted data
- Forgetting to check constraints first

---

## 5-Minute Revision

Clue words → Pattern → Template → Dry run → Complexity
