# Subsequence And Dynamic Programming Pattern Theory

## Core mental model

Substring means contiguous. Subsequence means order is preserved but characters
can be skipped.

## Recognition clues

- "delete some characters"
- "preserve relative order"
- "number of ways"
- "longest common"

## Common approaches

- Two pointers for yes/no matching.
- Preprocessed next-position lists for many queries.
- 1D or 2D DP for counting/optimization.

## Important variations

- Single query subsequence check
- Many word queries against one large string
- Lexicographic tie-breaking
- Count ways to form target
- LCS recurrence

