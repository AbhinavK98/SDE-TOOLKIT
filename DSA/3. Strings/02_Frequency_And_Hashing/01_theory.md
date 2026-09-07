# Frequency And Hashing Pattern Theory

## Why this pattern matters

Many string problems ask whether two strings have the same character inventory
or the same structural mapping. Hashing turns repeated searching into constant
average-time lookup.

## Core mental model

1. Convert the string into a useful signature.
2. Compare signatures or store them in a map.
3. Keep the signature cheap: count array for limited alphabet, dict for general input.

## Recognition clues

- "Anagram", "permutation", "same pattern"
- "How many times"
- "First unique"
- "Group similar strings"

## Important variations

- Fixed alphabet counts
- Hash map counts for arbitrary characters
- Bidirectional mapping for isomorphic structures
- Tuple signature for grouping anagrams
- Heap/bucket/sort by frequency

