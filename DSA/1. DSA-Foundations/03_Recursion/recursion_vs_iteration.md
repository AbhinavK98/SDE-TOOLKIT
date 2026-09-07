# Recursion vs Iteration

| Aspect | Recursion | Iteration |
|--------|-----------|-----------|
| Structure | Natural for trees | Natural for linear |
| Space | O(depth) stack | O(1) often |
| Speed | Call overhead | Usually faster |
| Debugging | Harder | Easier |

## HOW to convert recursion to iteration

Use explicit **stack** storing (parameters, state).

Factorial iterative:
```python
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
```

## WHEN interviewers prefer iteration

- Deep recursion risk
- Python (no TCO)
- Production code paths

## WHEN recursion is expected

- Tree traversal
- Backtracking
- Clear subproblem structure
