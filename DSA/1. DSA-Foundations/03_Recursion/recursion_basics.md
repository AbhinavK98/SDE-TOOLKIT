# Recursion Basics

---

## What is recursion?

A function **calls itself** with a smaller or simpler input until it hits a **base case** that stops the chain.

---

## Why recursion works

1. **Base case** — stops infinite calls.
2. **Progress** — each call moves toward base case.
3. **Trust** — assume subcall returns correct answer (recursive leap of faith).

---

## Call Stack and Stack Frames

**WHAT:** OS memory stack storing each active function call.

**HOW each frame stores:**
- Local variables
- Return address (where to continue after return)

```
main()
  └── factorial(4)
        └── factorial(3)
              └── factorial(2)
                    └── factorial(1)  <- base, returns 1
```

**WHY stack overflow:** Too many frames (infinite or very deep recursion).

---

## Base Case vs Recursive Case

| Part | Role |
|------|------|
| Base case | Simplest answer directly |
| Recursive case | Reduce problem + call self |

```python
def factorial(n: int) -> int:
    if n <= 1:          # BASE — WHY: stop recursion
        return 1
    return n * factorial(n - 1)  # RECURSIVE — smaller n
```

---

## How recursion returns

Returns unwind from deepest call upward:

```
factorial(3) waits for factorial(2)
factorial(2) waits for factorial(1) -> returns 1
factorial(2) returns 2*1=2
factorial(3) returns 3*2=6
```

---

## Decision Space

At each recursive step you **choose** (pick / skip, left / right). That creates a tree of possibilities — foundation of backtracking.

---

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| Missing base case | Write base first |
| Not progressing toward base | Ensure n decreases |
| Wrong return combination | Trace one small example |
| Global mutable state bugs | Pass state as parameters |

---

## Infinite recursion & Stack Overflow

**WHY:** No base case or no progress → calls never stop.

Python default recursion limit ~1000. Use iteration or `sys.setrecursionlimit` only when you understand risks.

---

## Memory usage

Each call = one stack frame. Depth d → O(d) space.

---

## References

Inspired by community recursion roadmaps; original explanations here.  
External reference: [Become Master in Recursion (LeetCode Discuss)](https://leetcode.com/discuss/post/1733447/become-master-in-recursion/)
