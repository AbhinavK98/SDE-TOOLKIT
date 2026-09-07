# Big O Deep Dive

Each complexity with **WHY / HOW / WHEN / WHAT**.

---

## O(1) — Constant Time

**WHAT:** Work does not grow with n.

**WHY fast:** Fixed number of steps.

**HOW recognize:** No loop over n; array index access `arr[i]`.

```python
def first(arr: list) -> int:
    return arr[0]  # O(1)
```

**WHEN:** Hash map lookup (average), stack push/pop.

**Analogy:** Opening one specific locker when you know the number.

---

## O(log n) — Logarithmic

**WHAT:** Doubling n adds one step.

**WHY:** Problem size **halves** each step (binary search).

**Dry run:** n=8, steps=3 (8→4→2→1).

```
Index: 0 1 2 3 4 5 6 7
              mid=3, then shrink...
```

---

## O(n) — Linear

**WHAT:** One pass through data.

```python
def sum_arr(arr):
    total = 0
    for x in arr:  # n iterations
        total += x
    return total
```

**WHY:** Each element processed once.

---

## O(n log n) — Linearithmic

**WHAT:** Typical of efficient comparison sorts.

**WHY:** log n divide levels × n work per level.

**WHEN:** Sorting general data when O(n²) is too slow.

---

## O(n²) — Quadratic

**WHAT:** Nested loops over n.

```python
for i in range(n):
    for j in range(n):
        ...
```

**WHEN acceptable:** n ≤ 5000 sometimes; n ≤ 10^5 never.

---

## O(2^n) — Exponential

**WHAT:** Branching choices (often subsets).

**WHEN:** n ≤ 20-25 in constraints hints backtracking.

---

## O(n!) — Factorial

**WHAT:** All permutations.

**WHEN:** n ≤ 10 typically.

---

## Code examples comparison

| Code pattern | Complexity |
|--------------|------------|
| Single loop | O(n) |
| Two nested loops | O(n²) |
| Loop + binary search inside | O(n log n) |
| Sort + loop | O(n log n) |
| Recursion 2 branches depth n | O(2^n) |
