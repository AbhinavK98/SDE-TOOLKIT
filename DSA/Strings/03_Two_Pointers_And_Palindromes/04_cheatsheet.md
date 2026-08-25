# Two Pointers And Palindromes Pattern Cheatsheet

## Template

```python
left, right = 0, len(s) - 1
while left < right:
    if s[left] != s[right]:
        return False
    left += 1
    right -= 1
return True
```

```python
def expand(left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return left + 1, right - 1
```

## Common variations

| Variant | Pointer movement |
|---|---|
| Valid palindrome | skip invalid, compare ends |
| One deletion | branch once at mismatch |
| Reverse vowels | each pointer seeks vowel |
| Palindromic substring | expand around centers |

