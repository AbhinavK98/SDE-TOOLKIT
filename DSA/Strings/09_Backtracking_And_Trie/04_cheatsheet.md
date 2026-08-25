# Backtracking And Trie Pattern Cheatsheet

## Backtracking template

```python
def backtrack(index, path):
    if index == len(s):
        answer.append(path[:])
        return
    for choice in choices:
        if valid(choice):
            path.append(choice)
            backtrack(next_index, path)
            path.pop()
```

## Trie template

```python
node = root
for ch in word:
    if ch not in node.children:
        node.children[ch] = TrieNode()
    node = node.children[ch]
node.is_word = True
```

## Pattern Comparison

| Variant | Core state |
|---|---|
| Letter combinations | digit index + path |
| Generate parentheses | open count + close count |
| Restore IP | index + parts |
| Word break | start index |
| Trie | current prefix node |

