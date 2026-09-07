# Basic String Manipulation Pattern Theory

This pattern builds comfort with strings as indexed sequences.

## Why this pattern matters

Most advanced string problems still depend on simple operations: scan once,
compare characters, reverse a range, skip spaces, and build output efficiently.

## Core mental model

1. Identify what part of the string is being read.
2. Decide whether output can be built directly or needs a mutable list.
3. Move pointers carefully around boundaries.
4. Avoid repeated string concatenation inside long loops.

## Recognition clues

- "Reverse the string / words / every k characters"
- "Remove spaces"
- "Common prefix"
- "Last word"
- No hidden optimal data structure is needed

## Important variations

- In-place character array modification
- Reverse fixed-size chunks
- Normalize spaces before reversing words
- Compare all strings column by column

## How to explain in interview

Start with a direct scan. Mention that Python strings are immutable, so repeated
character edits should use a list. State exactly which pointer owns which
boundary.

