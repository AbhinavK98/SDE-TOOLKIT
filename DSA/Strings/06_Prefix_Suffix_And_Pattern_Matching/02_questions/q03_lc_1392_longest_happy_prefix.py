"""LeetCode #1392 - Longest Happy Prefix.
Question Link: https://leetcode.com/problems/longest-happy-prefix/
"""


class BruteForce:
    def solve(self, s: str) -> str:
        for length in range(len(s) - 1, 0, -1):
            if s[:length] == s[-length:]:
                return s[:length]
        return ''


# Complexity (BruteForce)
#   Time:  O(n^2) — compare prefix/suffix for many lengths.
#   Space: O(n) — slicing creates temporary strings.


class BetterSolution:
    def solve(self, s: str) -> str:
        lps = self._build_lps(s)
        return s[:lps[-1]]

    def _build_lps(self, pattern: str) -> list[int]:
        lps = [0] * len(pattern)
        length = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            elif length:
                length = lps[length - 1]
            else:
                i += 1
        return lps


# Complexity (BetterSolution / OptimalSolution)
#   Time:  O(n) — final LPS value gives longest happy prefix.
#   Space: O(n) — LPS table.


class OptimalSolution(BetterSolution):
    pass

