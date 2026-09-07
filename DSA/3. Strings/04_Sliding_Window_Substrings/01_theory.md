# Sliding Window Substrings Pattern Theory

## Why this pattern matters

Brute force checks many substrings from scratch. Sliding window updates the
current substring as one character enters and another leaves.

## Core mental model

1. Expand `right`.
2. Add `s[right]` to window state.
3. Shrink `left` while the invariant is broken or while a valid window can improve.
4. Update the answer at the correct moment.

## Fixed vs variable window

- Fixed window: window length is exactly `k`.
- Variable window: length changes until counts/constraints become valid.

## Recognition clues

- "substring" means contiguous.
- "longest/shortest" with repeated characters or required characters.
- "permutation/anagram exists inside another string".

## Common approaches

- Set or last-seen index for no duplicates.
- Frequency maps for inclusion/anagram/min-window.
- Count of missing/formed characters to avoid full map comparison.

