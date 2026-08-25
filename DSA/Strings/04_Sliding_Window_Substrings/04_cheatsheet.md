# Sliding Window Substrings Pattern Cheatsheet

## Variable window template

```python
left = 0
for right in range(len(s)):
    add s[right]
    while window_invalid:
        remove s[left]
        left += 1
    update_answer()
```

## Fixed window template

```python
for right in range(len(s)):
    add s[right]
    if right >= k:
        remove s[right - k]
    if right >= k - 1:
        update_answer()
```

## Pattern Comparison

| Variant | Window state |
|---|---|
| No repeats | last seen index or set |
| Anagram | frequency difference |
| Minimum cover | need/have counts |
| Replacement | max frequency in window |
| Fixed score | running count/sum |

