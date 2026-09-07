# Stack Parsing And Construction Pattern Cheatsheet

## Template

```python
stack = []
for ch in s:
    if should_push(ch):
        stack.append(ch)
    elif should_pop(ch):
        stack.pop()
return build_answer(stack)
```

## Pattern Comparison

| Variant | Stack stores |
|---|---|
| Parentheses | opening brackets |
| Duplicate removal | kept characters |
| Decode string | previous string and count |
| Path | valid directory names |
| Calculator | signed numbers |

