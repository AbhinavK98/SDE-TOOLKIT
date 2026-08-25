# Subsequence And Dynamic Programming Pattern Cheatsheet

## Two pointer template

```python
i = 0
for ch in t:
    if i < len(s) and s[i] == ch:
        i += 1
return i == len(s)
```

## DP recognition

| Question asks | Common DP meaning |
|---|---|
| count ways | add choices |
| longest common | max choices |
| transform/delete | edit-style state |

## Common complexities

- One subsequence check: O(n)
- Many checks by buckets: O(total characters)
- LCS: O(mn) time, O(min(m, n)) possible space

