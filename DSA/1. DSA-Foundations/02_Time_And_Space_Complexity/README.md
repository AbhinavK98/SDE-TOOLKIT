# Time and Space Complexity

## What is it?

A language to describe how fast an algorithm runs and how much memory it uses as input grows.

## Why do we need it?

Interviewers need to compare solutions. Big O lets you reason without running code on huge inputs.

## Real-world analogy

Time = how long a line at a coffee shop takes as more people arrive. Space = how many chairs you need for waiting customers.

## Visualization

```
n grows -> operations grow?
O(1) flat | O(n) linear | O(n^2) steep curve
```

## Where interviewers ask it

Every coding round. 'What is the complexity?' is guaranteed.

## Advantages

- Predict scalability
- Compare algorithms fairly
- Spot bottlenecks

## Disadvantages

- Ignores constants (sometimes O(n) with huge constant loses to O(n log n))

## When NOT to use it

Tiny fixed n (n≤10) — any approach may work; still explain for habit.

## Interview Tricks

- Count loop nesting
- Ask 'what grows with n?'
- Recursion -> tree depth

## Cheat Sheet

See [Cheat Sheet](cheat_sheet.md)

## Revision Notes

- **5 min**: Read section headers + one dry run.
- **1 min**: Recall WHY / HOW / WHEN / WHAT for this topic.
- **Before interview**: Skim cheat sheet + common mistakes.

## Files in this section

- [theory.md](theory.md)
- [big_o.md](big_o.md)
- [complexity_comparison.md](complexity_comparison.md)
- [complexity_charts.md](complexity_charts.md)
- [cheat_sheet.md](cheat_sheet.md)
