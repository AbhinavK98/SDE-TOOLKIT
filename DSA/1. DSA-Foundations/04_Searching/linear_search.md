# Linear Search

## WHAT
Check each element until found or end.

## WHY
Works on any data — no sorting needed.

## WHEN
- Unsorted small array
- Linked list (no random access)
- One-time search

## Algorithm

```
for i in 0..n-1:
    if arr[i] == target: return i
return -1
```

## Dry Run

`[4, 2, 7, 1]`, target=7 → i=0 no, i=1 no, i=2 yes → return 2

## Complexity

Time O(n), Space O(1)

## Common Mistakes

- Returning wrong index on not found
- Not handling empty array
