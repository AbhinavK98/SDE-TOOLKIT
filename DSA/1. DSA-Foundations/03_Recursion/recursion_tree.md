# Recursion Tree

---

## WHAT

A diagram showing every recursive call as a node. Helps compute **time complexity**.

---

## Example: Fibonacci (naive)

```
                    fib(5)
                   /      \
              fib(4)        fib(3)
             /    \        /    \
        fib(3) fib(2)  fib(2) fib(1)
```

**WHY slow:** Repeated subproblems → O(2^n) nodes.

**WHEN to use tree:** Count calls, see overlap, decide memoization.

---

## Example: Merge sort

```
        sort(n)
       /       \
   sort(n/2)  sort(n/2)
```

Depth log n, each level O(n) work → **O(n log n)**.

---

## HOW to analyze

1. Draw tree for small n.
2. Count depth (height).
3. Count work per node.
4. Multiply or sum per level.

---

## ASCII: Call stack vs Tree

**Tree** = logical structure of calls  
**Stack** = actual execution order (depth-first)

```
Tree:          Stack (bottom to top):
   f(3)         f(1)
  /    \        f(2)
 f(2) f(1)       f(3)
```
