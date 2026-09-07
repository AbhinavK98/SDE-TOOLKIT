# Recursion Cheat Sheet

## 1-Minute

Base case + progress + trust subcall. Stack space = depth.

## 5-Minute

- IBH: Imagine, Base, Hypothesis
- Tree recursion → draw tree
- Backtrack = choose, explore, undo
- D&C = split, solve, merge

## Templates

See [recursion_templates.md](recursion_templates.md)

## Common Mistakes

- No base case
- Not undoing in backtracking
- Fibonacci without memo

## Pattern Recognition

| Problem | Pattern |
|---------|---------|
| All subsets | Include/exclude |
| All perms | Choose from remaining |
| Tree walk | DFS recursion |
| Split in half | Divide & conquer |
