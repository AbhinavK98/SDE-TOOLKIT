# Basic String Manipulation Pattern Cheatsheet

## Recognition Clues

- Reverse / trim / word order / prefix / suffix
- Constraint allows O(n)
- Problem is mostly about indexing and boundaries

## Template

```python
chars = list(s)
left, right = 0, len(chars) - 1
while left < right:
    chars[left], chars[right] = chars[right], chars[left]
    left += 1
    right -= 1
answer = ''.join(chars)
```

## Complexity

| Operation | Typical time | Typical space |
|---|---:|---:|
| Scan string | O(n) | O(1) |
| Build new string | O(n) | O(n) |
| In-place char list reverse | O(n) | O(1) extra |

## Common Mistakes

- Concatenating one character at a time in a loop
- Forgetting trailing spaces
- Off-by-one in chunk reversal
- Treating Python string like a mutable array

