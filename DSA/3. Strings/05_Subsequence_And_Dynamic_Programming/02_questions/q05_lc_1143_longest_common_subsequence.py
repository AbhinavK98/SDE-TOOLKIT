"""LeetCode #1143 - Longest Common Subsequence.
Question Link: https://leetcode.com/problems/longest-common-subsequence/
"""


class BruteForce:
    def solve(self, text1: str, text2: str) -> int:
        return self._lcs(text1, text2, 0, 0)

    def _lcs(self, a: str, b: str, i: int, j: int) -> int:
        if i == len(a) or j == len(b):
            return 0
        if a[i] == b[j]:
            return 1 + self._lcs(a, b, i + 1, j + 1)
        return max(self._lcs(a, b, i + 1, j), self._lcs(a, b, i, j + 1))


# Complexity (BruteForce)
#   Time:  O(2^(n+m)) — overlapping skip choices repeat heavily.
#   Space: O(n + m) — recursion depth.


class BetterSolution:
    def solve(self, text1: str, text2: str) -> int:
        previous = [0] * (len(text2) + 1)
        for i in range(len(text1) - 1, -1, -1):
            current = [0] * (len(text2) + 1)
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    current[j] = 1 + previous[j + 1]
                else:
                    current[j] = max(previous[j], current[j + 1])
            previous = current
        return previous[0]


# Complexity (BetterSolution / OptimalSolution)
#   Time:  O(n*m) — fill each DP state once.
#   Space: O(m) — only next row is kept.


class OptimalSolution(BetterSolution):
    pass

