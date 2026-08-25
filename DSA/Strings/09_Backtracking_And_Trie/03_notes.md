# Backtracking And Trie Pattern Notes

## Revision in 5 minutes

- Define the state: index, path, remaining open/close count, or trie node.
- Add only valid choices.
- Undo the choice after recursion.
- Memoize repeated suffix decisions in word break.
- Trie avoids checking every word for every prefix.

## Common mistakes

- Forgetting to pop from path.
- Allowing invalid IP segments with leading zeroes.
- Searching beyond trie prefix.
- Revisiting the same board cell in Word Search II.

## Revision in 1 minute

- Generate choices -> backtrack. Many prefix checks -> trie.

