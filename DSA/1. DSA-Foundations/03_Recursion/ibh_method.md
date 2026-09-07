# IBH Method (Imagine, Base, Hypothesis)

A beginner-friendly way to write recursion **without panic**.

---

## I — Imagine

**WHAT:** Assume the recursive function already works for smaller inputs.

**WHY:** You cannot prove every step while writing; trust the subproblem.

**Example:** `print_1_to_n(n)` — imagine `print_1_to_n(n-1)` already prints 1..n-1.

---

## B — Base

**WHAT:** Smallest input you can answer directly.

**HOW:** `if n == 1: print(1); return`

**WHY:** Stops recursion.

---

## H — Hypothesis / Build

**WHAT:** Use result of smaller call + one step of your own work.

**Example print 1 to n:**
```python
def print_1_to_n(n: int) -> None:
    if n == 1:
        print(1)
        return
    print_1_to_n(n - 1)  # hypothesis: prints 1..n-1
    print(n)               # my work
```

---

## Dry run print_1_to_n(3)

```
print_1_to_n(3)
  print_1_to_n(2)
    print_1_to_n(1)
      print 1
    print 2
  print 3
Output: 1 2 3
```

---

## WHEN to use IBH

Every new recursive problem in interviews. Say it aloud: "Base is..., I assume f(n-1) works, then I..."
