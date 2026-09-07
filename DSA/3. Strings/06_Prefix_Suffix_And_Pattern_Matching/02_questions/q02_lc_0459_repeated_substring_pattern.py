"""LeetCode #459 - Repeated Substring Pattern.
Question Link: https://leetcode.com/problems/repeated-substring-pattern/
"""


class BruteForce:
    def solve(self, s: str) -> bool:
        n = len(s)
        for length in range(1, n // 2 + 1):
            if n % length == 0 and s[:length] * (n // length) == s:
                return True
        return False


# Complexity (BruteForce)
#   Time:  O(n^2) — test possible pattern lengths by rebuilding strings.
#   Space: O(n) — repeated candidate string.


class BetterSolution:
    def solve(self, s: str) -> bool:
        doubled = (s + s)[1:-1]
        return s in doubled


# Complexity (BetterSolution)
#   Time:  O(n) average — substring search over doubled string.
#   Space: O(n) — doubled string.


class OptimalSolution:
    def solve(self, s: str) -> bool:
        lps = self._build_lps(s)
        longest = lps[-1]
        return longest > 0 and len(s) % (len(s) - longest) == 0

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


# Complexity (OptimalSolution)
#   Time:  O(n) — build one LPS table.
#   Space: O(n) — LPS table.

