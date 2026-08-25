"""LeetCode #214 - Shortest Palindrome.
Question Link: https://leetcode.com/problems/shortest-palindrome/
"""


class BruteForce:
    def solve(self, s: str) -> str:
        for end in range(len(s), -1, -1):
            prefix = s[:end]
            if prefix == prefix[::-1]:
                return s[end:][::-1] + s
        return s


# Complexity (BruteForce)
#   Time:  O(n^2) — check each prefix palindrome by reversing.
#   Space: O(n) — slices and reversed strings.


class BetterSolution:
    def solve(self, s: str) -> str:
        combined = s + '#' + s[::-1]
        lps = self._build_lps(combined)
        pal_prefix_len = lps[-1]
        return s[pal_prefix_len:][::-1] + s

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
#   Time:  O(n) — KMP over combined string.
#   Space: O(n) — combined string and LPS table.


class OptimalSolution(BetterSolution):
    pass

