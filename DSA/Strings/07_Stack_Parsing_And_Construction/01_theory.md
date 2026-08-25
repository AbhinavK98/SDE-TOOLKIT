# Stack Parsing And Construction Pattern Theory

## Core mental model

A stack remembers unfinished work. When a closing token, deletion marker, or
operator arrives, resolve the most recent unfinished piece first.

## Recognition clues

- Nested brackets or encoded sections
- "remove adjacent"
- Backspace/cancellation
- Unix path tokens
- Expression with precedence

## Important variations

- Character stack
- Pair stack with counts
- Token stack
- Build result while resolving operators
- Two-pointer reverse scan to avoid materializing stacks

