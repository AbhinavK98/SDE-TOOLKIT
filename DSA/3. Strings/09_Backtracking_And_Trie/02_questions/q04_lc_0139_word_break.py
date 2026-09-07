"""LeetCode #139 - Word Break.
Question Link: https://leetcode.com/problems/word-break/
"""
from typing import List


class BruteForce:
    def solve(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        return self._can_break(s, words, 0)

    def _can_break(self, s: str, words: set[str], start: int) -> bool:
        if start == len(s):
            return True
        for end in range(start + 1, len(s) + 1):
            if s[start:end] in words and self._can_break(s, words, end):
                return True
        return False


# Complexity (BruteForce)
#   Time:  O(2^n) — repeated suffix decisions.
#   Space: O(n) — recursion depth.


class BetterSolution:
    def solve(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        memo = {}
        return self._can_break(s, words, 0, memo)

    def _can_break(self, s: str, words: set[str], start: int, memo: dict[int, bool]) -> bool:
        if start == len(s):
            return True
        if start in memo:
            return memo[start]
        for end in range(start + 1, len(s) + 1):
            if s[start:end] in words and self._can_break(s, words, end, memo):
                memo[start] = True
                return True
        memo[start] = False
        return False


# Complexity (BetterSolution / OptimalSolution)
#   Time:  O(n^3) — n starts, n ends, slicing costs up to n.
#   Space: O(n) — memo and recursion depth.


class OptimalSolution(BetterSolution):
    pass

