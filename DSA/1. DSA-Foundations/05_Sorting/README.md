# Sorting

## What is it?

Arranging elements in order (usually ascending).

## Why do we need it?

Sorted data unlocks binary search, two pointers, merge patterns, and efficient processing.

## Real-world analogy

Sorting books on shelf by title — different methods: swap neighbors (bubble), pick smallest remaining (selection), insert into sorted section (insertion).

## Visualization

```
Before: 5 4 2 1
After pass: 4 2 1 5 (bubble example)
```

## Where interviewers ask it

Almost every interview domain; also 'sort then solve' trick.

## Advantages

- Enables O(log n) search
- Simplifies duplicate handling

## Disadvantages

- O(n log n) comparison sort lower bound
- Destroys original order unless stable

## When NOT to use it

When only need top-k (use heap) or counting sort on small range.

## Interview Tricks

- Ask: stable? in-place? worst case?

## Cheat Sheet

See [Cheat Sheet](cheat_sheet.md)

## Revision Notes

- **5 min**: Read section headers + one dry run.
- **1 min**: Recall WHY / HOW / WHEN / WHAT for this topic.
- **Before interview**: Skim cheat sheet + common mistakes.

## Files in this section

- [bubble_sort.md](bubble_sort.md)
- [selection_sort.md](selection_sort.md)
- [insertion_sort.md](insertion_sort.md)
- [merge_sort.md](merge_sort.md)
- [quick_sort.md](quick_sort.md)
- [heap_sort.md](heap_sort.md)
- [comparison_table.md](comparison_table.md)
- [cheat_sheet.md](cheat_sheet.md)
