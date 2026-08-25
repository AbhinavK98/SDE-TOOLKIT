"""LeetCode #524 - Longest Word in Dictionary through Deleting.
Question Link: https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/
"""
from typing import List


class BruteForce:
    def solve(self, s: str, dictionary: List[str]) -> str:
        best = ''
        for word in dictionary:
            if self._is_subsequence(word, s):
                if len(word) > len(best) or (len(word) == len(best) and word < best):
                    best = word
        return best

    def _is_subsequence(self, word: str, s: str) -> bool:
        i = 0
        for ch in s:
            if i < len(word) and word[i] == ch:
                i += 1
        return i == len(word)


# Complexity (BruteForce / OptimalSolution)
#   Time:  O(d*n) — scan s for each dictionary word.
#   Space: O(1) — excluding input and output.


class OptimalSolution(BruteForce):
    pass

