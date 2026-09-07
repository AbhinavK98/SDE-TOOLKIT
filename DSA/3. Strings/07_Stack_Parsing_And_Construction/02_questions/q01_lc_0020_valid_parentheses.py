"""LeetCode #20 - Valid Parentheses.
Question Link: https://leetcode.com/problems/valid-parentheses/
"""


class BruteForce:
    def solve(self, s: str) -> bool:
        previous = None
        while previous != s:
            previous = s
            s = s.replace('()', '').replace('[]', '').replace('{}', '')
        return s == ''


# Complexity (BruteForce)
#   Time:  O(n^2) — repeated replace scans the shrinking string.
#   Space: O(n) — strings are rebuilt.


class BetterSolution:
    def solve(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}
        for ch in s:
            if ch in pairs.values():
                stack.append(ch)
            elif not stack or stack.pop() != pairs[ch]:
                return False
        return not stack


# Complexity (BetterSolution / OptimalSolution)
#   Time:  O(n) — each bracket is pushed or popped once.
#   Space: O(n) — stack stores unmatched open brackets.


class OptimalSolution(BetterSolution):
    pass

