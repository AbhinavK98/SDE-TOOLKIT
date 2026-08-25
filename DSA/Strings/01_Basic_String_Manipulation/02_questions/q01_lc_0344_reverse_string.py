"""LeetCode #344 - Reverse String.
Question Link: https://leetcode.com/problems/reverse-string/
"""
from typing import List


class BruteForce:
    def solve(self, s: List[str]) -> None:
        reversed_chars = s[::-1]
        for i in range(len(s)):
            s[i] = reversed_chars[i]


# Complexity (BruteForce)
#   Time:  O(n) — copy and rewrite all characters.
#   Space: O(n) — reversed copy stores n characters.


class BetterSolution:
    def solve(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


# Complexity (BetterSolution / OptimalSolution)
#   Time:  O(n) — each character is swapped at most once.
#   Space: O(1) — in-place reversal.


class OptimalSolution(BetterSolution):
    pass

