# Recursion Practice Questions

Each problem: Problem → Thinking → Visualization → Dry Run → Complexity.

---

## 1. Print 1 to N

**Thinking:** Print 1..n-1 first (hypothesis), then n.

```python
def print_1_to_n(n: int) -> None:
    if n == 1:
        print(1)
        return
    print_1_to_n(n - 1)
    print(n)
```

**Complexity:** Time O(n), Space O(n) stack.

---

## 2. Print N to 1

**Thinking:** Print n first (head), then n-1..1.

```python
def print_n_to_1(n: int) -> None:
    if n == 0:
        return
    print(n)
    print_n_to_1(n - 1)
```

---

## 3. Factorial

**Base:** 0! = 1! = 1  
**Recurrence:** n! = n × (n-1)!

**Dry run n=4:** 4×3×2×1 = 24

**Complexity:** O(n) time, O(n) space.

---

## 4. Power(x, n)

**Thinking:** x^n = x^(n/2) × x^(n/2) for even n.

```python
def power(x: float, n: int) -> float:
    if n == 0:
        return 1.0
    if n < 0:
        return 1.0 / power(x, -n)
    half = power(x, n // 2)
    if n % 2 == 0:
        return half * half
    return half * half * x
```

**Complexity:** O(log n)

---

## 5. Fibonacci

Naive: T(n)=T(n-1)+T(n-2) → O(2^n)  
Memoized: O(n)

---

## 6. Reverse String

```python
def reverse_string(s: list, left: int, right: int) -> None:
    if left >= right:
        return
    s[left], s[right] = s[right], s[left]
    reverse_string(s, left + 1, right - 1)
```

---

## 7. Palindrome

Compare ends, recurse inward. Base: left >= right.

---

## 8. Subset Generation

```
        []
       /  \
     [1]  []
    / \  / \
  [1,2][1][2][]
```

Include / exclude each element at index i.

---

## 9. Permutations

Choose unused element at each position. Backtrack after placing.

---

## 10. Tower of Hanoi

Move n-1 to auxiliary, move largest, move n-1 to target.  
**Moves:** 2^n - 1

---

## 11. Sort Array (Merge Sort)

Divide half, sort each, merge. O(n log n).

---

## 12-14. Stack Recursion (Sort / Reverse / Delete Middle)

Use recursion to reach bottom of stack, operate on way up.

---

## 15. Generate Parentheses

Backtrack: add '(' if open < n, add ')' if close < open.

---

## 16. Letter Case Permutation

At each char: branch if letter (upper/lower), else continue.

---

## Interview Questions (common)

- Can you do it iteratively?
- What is stack depth?
- How to optimize overlapping subproblems? (memoization)
