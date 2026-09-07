# Subsequence And Dynamic Programming Pattern Notes

## Revision in 5 minutes

- Single subsequence check -> two pointers.
- Many checks -> preprocess or bucket waiting words.
- Count ways -> DP over source and target.
- LCS -> if equal, take diagonal + 1; else max of skip one side.
- Tie-breaking often matters for dictionary deletion problems.

## Common mistakes

- Confusing substring with subsequence.
- Resetting source pointer for every word when many queries exist.
- Updating 1D DP left-to-right when recurrence needs previous row values.

## Revision in 1 minute

- Preserve order, skip allowed. Yes/no -> pointers. Count/best -> DP.

