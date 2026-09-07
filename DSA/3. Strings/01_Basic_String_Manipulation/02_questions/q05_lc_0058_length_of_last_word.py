"""LeetCode #58 - Length of Last Word.
Question Link: https://leetcode.com/problems/length-of-last-word/
"""


class BruteForce:
    def solve(self, s: str) -> int:
        words = s.split()
        return len(words[-1]) if words else 0


# Complexity (BruteForce)
#   Time:  O(n) — split scans the whole string.
#   Space: O(n) — words list stores all tokens.


class BetterSolution:
    def solve(self, s: str) -> int:
        i = len(s) - 1
        while i >= 0 and s[i] == ' ':
            i -= 1
        length = 0
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1
        return length


# Complexity (BetterSolution / OptimalSolution)
#   Time:  O(n) — scans from the end until the last word is counted.
#   Space: O(1) — only counters are used.


class OptimalSolution(BetterSolution):
    pass

