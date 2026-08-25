"""LeetCode #392 - Is Subsequence.
Question Link: https://leetcode.com/problems/is-subsequence/
"""


class BruteForce:
    def solve(self, s: str, t: str) -> bool:
        position = -1
        for ch in s:
            position = t.find(ch, position + 1)
            if position == -1:
                return False
        return True


# Complexity (BruteForce)
#   Time:  O(n*m) — repeated find can rescan the target string.
#   Space: O(1) — only current position.


class BetterSolution:
    def solve(self, s: str, t: str) -> bool:
        i = 0
        for ch in t:
            if i < len(s) and s[i] == ch:
                i += 1
        return i == len(s)


# Complexity (BetterSolution / OptimalSolution)
#   Time:  O(m) — scan t once.
#   Space: O(1) — one pointer into s.


class OptimalSolution(BetterSolution):
    pass

