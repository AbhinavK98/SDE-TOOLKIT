"""LeetCode #14 - Longest Common Prefix.
Question Link: https://leetcode.com/problems/longest-common-prefix/
"""
from typing import List


class BruteForce:
    def solve(self, strs: List[str]) -> str:
        if not strs:
            return ''
        prefix = strs[0]
        for word in strs[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ''
        return prefix


# Complexity (BruteForce)
#   Time:  O(n*m^2) — repeated prefix slicing/checking can rescan characters.
#   Space: O(m) — prefix slicing creates temporary strings.


class BetterSolution:
    def solve(self, strs: List[str]) -> str:
        if not strs:
            return ''
        for i in range(len(strs[0])):
            current = strs[0][i]
            for word in strs[1:]:
                if i == len(word) or word[i] != current:
                    return strs[0][:i]
        return strs[0]


# Complexity (BetterSolution / OptimalSolution)
#   Time:  O(n*m) — compare each column across strings until mismatch.
#   Space: O(1) — ignoring returned prefix.


class OptimalSolution(BetterSolution):
    pass

