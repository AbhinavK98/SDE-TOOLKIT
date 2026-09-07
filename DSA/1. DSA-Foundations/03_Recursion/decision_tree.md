# Recursion Decision Tree

```
Need to explore all choices?
├── Yes -> Backtracking recursion
│         (subsets, permutations, parentheses)
└── No -> Problem size halves each step?
          ├── Yes -> Divide & Conquer
          │         (merge sort, binary search)
          └── Linear decrease?
                    -> Simple linear recursion
                      (factorial, linked list)
```

## When to use recursion

- Tree / graph DFS
- Generate combinations
- Problem defined on substructure (left subtree, right subtree)

## When NOT to use

- Deep n (stack overflow)
- Simple loop suffices
- Tail-recursion not optimized in Python — prefer loop

## Head vs Tail vs Tree recursion

| Type | Call position | Example |
|------|---------------|---------|
| Head | Before recursive call | factorial |
| Tail | After recursive call (last op) | print n to 1 with tail idea |
| Tree | Multiple recursive calls | fibonacci naive |
