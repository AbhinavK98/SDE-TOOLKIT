# Prefix Suffix And Pattern Matching Pattern Cheatsheet

## LPS template

```python
lps = [0] * len(pattern)
length = 0
i = 1
while i < len(pattern):
    if pattern[i] == pattern[length]:
        length += 1
        lps[i] = length
        i += 1
    elif length:
        length = lps[length - 1]
    else:
        i += 1
```

## Pattern Comparison

| Pattern | Use when |
|---|---|
| KMP | exact pattern search, prefix-suffix structure |
| Z-algorithm | prefix match length at every index |
| Rolling hash | repeated substring comparison |

