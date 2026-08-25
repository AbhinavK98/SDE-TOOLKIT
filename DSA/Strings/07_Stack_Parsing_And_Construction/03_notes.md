# Stack Parsing And Construction Pattern Notes

## Revision in 5 minutes

- Parentheses -> push openers, match closers.
- Adjacent duplicate removal -> stack top decides cancellation.
- Decode string -> store previous string and repeat count before `[` .
- Path simplification -> ignore `.`, pop on `..`.
- Calculator -> apply previous operator when next operator arrives.

## Common mistakes

- Forgetting multi-digit numbers.
- Applying the current operator instead of the previous one.
- Mishandling empty stack on closing bracket.
- Joining path with missing leading slash.

## Revision in 1 minute

- Latest unresolved token matters -> stack.

