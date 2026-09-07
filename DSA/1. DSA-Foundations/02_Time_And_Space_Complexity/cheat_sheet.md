# Complexity Cheat Sheet

## 1-Minute Revision

- Count loops → nested depth
- Recursion → tree depth × work per node
- Sort = usually O(n log n)
- Hash = O(1) avg lookup
- BS = O(log n) on sorted data

## 5-Minute Revision

1. O(1), O(log n), O(n), O(n log n), O(n²), O(2^n)
2. Time vs auxiliary space
3. Nested loop = multiply
4. Sequential blocks = add (take max)
5. Amortized O(1) append

## Interview Notes

- State **worst case** unless asked otherwise
- Mention recursion stack in space
- "Dominated by the sort" if you call sort once

## Common Mistakes

- O(n + m) written as O(n) when both grow — OK to say O(n+m)
- Forgetting sort inside loop
- Best case as answer without clarification

## Pattern Recognition

| See | Think |
|-----|-------|
| Halving | log n |
| Single scan | n |
| All pairs | n² |
| Divide half + merge | n log n |
