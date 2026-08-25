"""LeetCode #49 - Group Anagrams.
Question Link: https://leetcode.com/problems/group-anagrams/
"""
from typing import List


class BruteForce:
    def solve(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            key = ''.join(sorted(word))
            groups.setdefault(key, []).append(word)
        return list(groups.values())


# Complexity (BruteForce)
#   Time:  O(n*m log m) — sort each word of length m.
#   Space: O(n*m) — grouped output and keys.


class BetterSolution:
    def solve(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            count = [0] * 26
            for ch in word:
                count[ord(ch) - ord('a')] += 1
            groups.setdefault(tuple(count), []).append(word)
        return list(groups.values())


# Complexity (BetterSolution / OptimalSolution)
#   Time:  O(total characters) — count each word once.
#   Space: O(n) — one signature per group plus output.


class OptimalSolution(BetterSolution):
    pass

