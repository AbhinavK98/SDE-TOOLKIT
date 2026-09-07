# Sliding Window Substrings Pattern Notes

## Revision in 5 minutes

- Decide fixed or variable window first.
- Track only what changes when right enters and left leaves.
- For min-window, update answer before shrinking loses validity.
- For longest valid window, update after restoring validity.
- For counting substrings, sometimes every extension to the right is valid.

## Common mistakes

- Updating answer before the window is valid.
- Shrinking with `if` when a `while` is needed.
- Comparing full frequency dictionaries every iteration.
- Forgetting duplicate characters in target strings.

## Revision in 1 minute

- Right expands. Left repairs. Counts describe the current substring.

