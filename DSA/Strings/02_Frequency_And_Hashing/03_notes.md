# Frequency And Hashing Pattern Notes

## Revision in 5 minutes

- Anagram -> equal counts.
- Ransom note -> required counts must never exceed available counts.
- Isomorphic / word pattern -> enforce both directions.
- Group anagrams -> sorted string or 26-count tuple as key.
- First unique -> count first, scan original order second.

## Common mistakes

- Only checking one direction in mapping problems.
- Using sorted keys when a count tuple is clearer for lowercase English letters.
- Forgetting that order matters for "first unique".
- Assuming alphabet size when constraints allow Unicode or mixed case.

## Revision in 1 minute

- Same inventory -> counts. Same structure -> two maps. Group -> canonical key.

