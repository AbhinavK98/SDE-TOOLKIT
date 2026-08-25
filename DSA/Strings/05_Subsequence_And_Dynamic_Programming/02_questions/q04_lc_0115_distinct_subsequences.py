"""LeetCode #115 - Distinct Subsequences.
Question Link: https://leetcode.com/problems/distinct-subsequences/
"""


class BruteForce:
    def solve(self, s: str, t: str) -> int:
        return self._count(s, t, 0, 0)

    def _count(self, s: str, t: str, i: int, j: int) -> int:
        if j == len(t):
            return 1
        if i == len(s):
            return 0
        total = self._count(s, t, i + 1, j)
        if s[i] == t[j]:
            total += self._count(s, t, i + 1, j + 1)
        return total


# Complexity (BruteForce)
#   Time:  O(2^n) — each source char can be skipped or used.
#   Space: O(n) — recursion depth.


class BetterSolution:
    def solve(self, s: str, t: str) -> int:
        dp = [0] * (len(t) + 1)
        dp[0] = 1
        for ch in s:
            for j in range(len(t) - 1, -1, -1):
                if ch == t[j]:
                    dp[j + 1] += dp[j]
        return dp[len(t)]


# Complexity (BetterSolution / OptimalSolution)
#   Time:  O(n*m) — process every source-target state once.
#   Space: O(m) — one DP row.


class OptimalSolution(BetterSolution):
    pass

