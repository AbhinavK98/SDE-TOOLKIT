# Two Pointers And Palindromes Pattern Theory

## Core mental model

Palindromes are symmetric. Compare the outside first, or expand from the center
and keep matching while both sides stay equal.

## Recognition clues

- "Palindrome"
- "Can delete at most one"
- "Reverse only selected characters"
- "Count/longest palindromic substring"

## Important variations

- Converging pointers from both ends
- Skip invalid characters
- Branch once on mismatch
- Expand around odd and even centers

## Time/space considerations

End-to-end comparison is O(n). Expanding around every center is O(n^2) time and
O(1) space, which is usually accepted for palindrome substring problems.

