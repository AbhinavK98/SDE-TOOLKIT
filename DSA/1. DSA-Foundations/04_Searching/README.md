# Searching

## What is it?

Algorithms to find an element or answer in data.

## Why do we need it?

Raw scan is O(n). Binary search and variants achieve O(log n) when structure allows.

## Real-world analogy

Linear = check every book on shelf. Binary = phone book: open middle, discard half.

## Visualization

```
sorted: [1,3,5,7,9] mid=5, go left or right
```

## Where interviewers ask it

Sorted arrays, rotated arrays, answer space problems, boundaries.

## Advantages

- Huge speedup on sorted data
- Templates reusable

## Disadvantages

- Requires order or monotonic property
- Off-by-one bugs common

## When NOT to use it

Unsorted one-time search with no preprocessing — use hash map or linear.

## Interview Tricks

- Use lo, hi, mid; think inclusive vs exclusive bounds

## Cheat Sheet

See [Cheat Sheet](cheat_sheet.md)

## Revision Notes

- **5 min**: Read section headers + one dry run.
- **1 min**: Recall WHY / HOW / WHEN / WHAT for this topic.
- **Before interview**: Skim cheat sheet + common mistakes.

## Files in this section

- [linear_search.md](linear_search.md)
- [binary_search.md](binary_search.md)
- [binary_search_variations.md](binary_search_variations.md)
- [cheat_sheet.md](cheat_sheet.md)
