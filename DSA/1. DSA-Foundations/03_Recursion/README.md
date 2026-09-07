# Recursion

## What is it?

A function that solves a problem by calling itself on smaller subproblems until a base case is reached.

## Why do we need it?

Many structures (trees, graphs, combinations) are naturally recursive. Backtracking and divide-and-conquer depend on it.

## Real-world analogy

Russian nesting dolls: open one doll until you reach the smallest (base case), then close them back up (return values).

## Visualization

```
solve(n) -> solve(n-1) -> ... -> base -> return chain
```

## Where interviewers ask it

Trees, graphs, subsets, permutations, divide-and-conquer, DFS.

## Advantages

- Elegant for hierarchical data
- Matches problem structure

## Disadvantages

- Stack overflow risk
- Can be slower than iteration
- Harder to debug initially

## When NOT to use it

Simple linear scan; deep n (>10^4) recursion depth; tight memory.

## Interview Tricks

- Always define base case first
- Draw recursion tree
- Use IBH: Imagine, Base, Hypothesis

## Cheat Sheet

See [Cheat Sheet](cheat_sheet.md)

## Revision Notes

- **5 min**: Read section headers + one dry run.
- **1 min**: Recall WHY / HOW / WHEN / WHAT for this topic.
- **Before interview**: Skim cheat sheet + common mistakes.

## Files in this section

- [recursion_basics.md](recursion_basics.md)
- [recursion_tree.md](recursion_tree.md)
- [ibh_method.md](ibh_method.md)
- [decision_tree.md](decision_tree.md)
- [recursion_templates.md](recursion_templates.md)
- [recursion_vs_iteration.md](recursion_vs_iteration.md)
- [recursion_questions.md](recursion_questions.md)
- [cheat_sheet.md](cheat_sheet.md)
