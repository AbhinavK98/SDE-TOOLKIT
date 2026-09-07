# Frequency And Hashing Pattern Cheatsheet

## Recognition Clues

- count, frequency, anagram, pattern, unique, duplicate, group

## Templates

```python
count = {}
for ch in s:
    count[ch] = count.get(ch, 0) + 1
```

```python
key = [0] * 26
for ch in word:
    key[ord(ch) - ord('a')] += 1
signature = tuple(key)
```

## Pattern Comparison

| Problem type | Core idea | Complexity |
|---|---|---|
| Anagram | compare counts | O(n) |
| First unique | count then rescan | O(n) |
| Isomorphic | two-way map | O(n) |
| Group anagrams | map signature to list | O(total chars) |

