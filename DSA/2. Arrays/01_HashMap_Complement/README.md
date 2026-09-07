# HashMap Complement Pattern

## What is this pattern?

This pattern is a repeatable way of thinking about array problems.
Instead of trying random approaches, you identify the clue and apply a tested strategy.

Imagine solving problems with a small toolkit. If you pick the right tool quickly,
your solution becomes both faster and easier to explain in interviews.

## When should I use this pattern?

- Find pair / target sum
- Lookup in constant time
- Seen before checks
- Sorted array pointer movement
- Contiguous range optimization
- Running totals and range queries

## Pattern Visualization

```
Input Array -> Observe current element -> Ask what is needed
                             |
                             v
                    Store / Move / Expand / Shrink
                             |
                             v
                         Build Answer
```

## General Algorithm

1. Read the problem and list constraints.
2. Write brute force to prove correctness.
3. Identify repeated work and remove it.
4. Choose data structure/pointer strategy for optimal.
5. Dry run with edge cases.

## Time Complexity

Complexity comes from how many times we touch each element.
Optimal array patterns usually process each item once or twice, giving linear time.

## Space Complexity

Space depends on whether we store extra structures (hash map, prefix array) or solve in-place.

## Advantages

- Faster pattern recognition
- Cleaner interview communication
- Less trial-and-error coding

## Disadvantages

- Wrong pattern selection leads to dead ends
- Overusing one pattern can miss simpler solutions

## Common Interview Questions

- Can you do this in O(n)?
- Can you do this with O(1) extra space?
- What changes if input is sorted?
- What if duplicates are allowed?

## Common Mistakes

- Forgetting edge cases (empty/single element)
- Wrong pointer updates
- Hash map insertion order mistakes
- Off-by-one in prefix/slicing logic

## Dry Run

Example generic dry run:

- Iteration 1: inspect first value, initialize state.
- Iteration 2: update structure/pointers.
- Iteration n: finalize and return answer.

Always dry run with both normal and edge inputs.
