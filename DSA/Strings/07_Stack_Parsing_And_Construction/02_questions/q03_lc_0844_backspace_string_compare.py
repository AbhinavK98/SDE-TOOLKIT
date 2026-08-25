"""LeetCode #844 - Backspace String Compare.
Question Link: https://leetcode.com/problems/backspace-string-compare/
"""


class BruteForce:
    def solve(self, s: str, t: str) -> bool:
        return self._build(s) == self._build(t)

    def _build(self, text: str) -> str:
        stack = []
        for ch in text:
            if ch == '#':
                if stack:
                    stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)


# Complexity (BruteForce)
#   Time:  O(n + m) — build both final strings.
#   Space: O(n + m) — stacks store built strings.


class BetterSolution:
    def solve(self, s: str, t: str) -> bool:
        i, j = len(s) - 1, len(t) - 1
        while i >= 0 or j >= 0:
            i = self._next_valid(s, i)
            j = self._next_valid(t, j)
            if i < 0 or j < 0:
                return i == j
            if s[i] != t[j]:
                return False
            i -= 1
            j -= 1
        return True

    def _next_valid(self, text: str, index: int) -> int:
        skip = 0
        while index >= 0:
            if text[index] == '#':
                skip += 1
            elif skip:
                skip -= 1
            else:
                return index
            index -= 1
        return index


# Complexity (BetterSolution / OptimalSolution)
#   Time:  O(n + m) — reverse pointers scan each string once.
#   Space: O(1) — no built strings.


class OptimalSolution(BetterSolution):
    pass

