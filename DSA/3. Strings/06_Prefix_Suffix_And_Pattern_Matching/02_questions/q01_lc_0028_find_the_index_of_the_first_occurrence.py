"""LeetCode #28 - Find the Index of the First Occurrence in a String.
Question Link: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
"""


class BruteForce:
    def solve(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0
        n, m = len(haystack), len(needle)
        for i in range(n - m + 1):
            if haystack[i:i + m] == needle:
                return i
        return -1


# Complexity (BruteForce)
#   Time:  O(n*m) — each start can compare up to m characters.
#   Space: O(m) — slicing creates temporary strings.


class BetterSolution:
    def solve(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0
        lps = self._build_lps(needle)
        j = 0
        for i in range(len(haystack)):
            while j > 0 and haystack[i] != needle[j]:
                j = lps[j - 1]
            if haystack[i] == needle[j]:
                j += 1
                if j == len(needle):
                    return i - len(needle) + 1
        return -1

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
#   Time:  O(n + m) — KMP never moves text pointer backward.
#   Space: O(m) — LPS table for needle.


class OptimalSolution(BetterSolution):
    pass

