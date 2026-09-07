# Recursion Templates

## Template 1: Linear decrease

```python
def solve(n: int) -> int:
    if base_condition(n):
        return base_value
    return combine(n, solve(smaller(n)))
```

## Template 2: Backtracking

```python
def backtrack(state, choices):
    if complete(state):
        record(state)
        return
    for choice in choices:
        if valid(choice):
            apply(state, choice)
            backtrack(state, next_choices)
            undo(state, choice)  # CRITICAL
```

## Template 3: Divide and conquer

```python
def dc(arr, lo, hi):
    if lo >= hi:
        return base
    mid = (lo + hi) // 2
    left = dc(arr, lo, mid)
    right = dc(arr, mid + 1, hi)
    return merge(left, right)
```

## Interview templates

- Always state base case verbally
- Mention stack depth for space
- For subsets: include/exclude branch at each index
