# Time and Space Complexity — Theory

---

## What is Time Complexity?

**WHAT:** Upper bound on how the number of operations grows with input size `n`.

**WHY:** We cannot run code on billion-row inputs in an interview. We **reason** instead.

**HOW:** Count dominant operations in loops/recursion. Drop constants and lower terms.

**WHEN:** Every solution discussion.

---

## What is Space Complexity?

**WHAT:** Extra memory used beyond input storage (auxiliary space).

**WHY:** Memory is limited. In-place algorithms are prized when correct.

**HOW:** Count extra arrays, hash maps, recursion stack depth.

**Example:** Merge sort uses O(n) extra array. Quick sort in-place uses O(log n) stack on average.

---

## Why Big O exists

Computers differ (CPU, cache). Big O focuses on **growth rate** so analysis is machine-independent.

---

## Big O vs Theta vs Omega

| Notation | Meaning | Interview usage |
|----------|---------|-----------------|
| O (Big O) | Worst-case upper bound | **Most common** — "O(n)" |
| Ω (Omega) | Lower bound | Rare in interviews |
| Θ (Theta) | Tight bound | "Exactly Θ(n log n)" for merge sort |

**Interview default:** Say "O(...)" unless asked for tight bound.

---

## Growth rates (simple language)

| Complexity | Name | n=1000 rough ops | Analogy |
|------------|------|------------------|---------|
| O(1) | Constant | 1 | Flip light switch |
| O(log n) | Logarithmic | ~10 | Phone book halving |
| O(n) | Linear | 1000 | Scan every item once |
| O(n log n) | Linearithmic | ~10k | Efficient sorting |
| O(n²) | Quadratic | 1,000,000 | Every pair |
| O(2^n) | Exponential | huge | All subsets |
| O(n!) | Factorial | astronomical | All permutations |

---

## Nested loops

```python
for i in range(n):      # n
    for j in range(n):  # n
        work()          # O(1)
# Total: O(n^2)
```

**WHY:** Inner loop runs n times for each of n outer iterations.

---

## Recursion complexity

Time often = (work per call) × (number of calls).

Draw a **recursion tree**. See [../03_Recursion/recursion_tree.md](../03_Recursion/recursion_tree.md).

---

## Binary Search — O(log n)

Each step eliminates half the search space.

```
n -> n/2 -> n/4 -> ... -> 1
Steps ≈ log₂(n)
```

---

## Merge Sort — O(n log n)

Divide: log n levels. Merge at each level: O(n) total per level.

---

## DFS / BFS on graphs

- Time: O(V + E) — visit each vertex and edge once.
- Space: O(V) for visited set / queue / stack.

---

## HashMap operations

Average O(1) insert, lookup, delete. Worst O(n) with bad hashing (rare in interviews).

---

## Amortized Analysis (basic)

**WHAT:** Average cost over many operations.

**Example:** Dynamic array append — mostly O(1), occasionally O(n) resize. Amortized O(1).

---

## Master Theorem (basic)

For recurrences like T(n) = aT(n/b) + O(n^d):

Used to get complexity of divide-and-conquer without drawing full tree.

**Interview:** Know merge sort and binary search recurrences; deep Master Theorem is optional.

---

## How interviewers calculate complexity

1. Identify basic operation (comparison, assignment).
2. Count how many times it runs as function of n.
3. Keep highest order term.
4. Drop constants: 3n² + 5n → O(n²).

---

## Common Mistakes

- Confusing best case with Big O (usually worst case)
- Forgetting hidden loops (`sort` inside loop → O(n² log n))
- Ignoring recursion stack space
