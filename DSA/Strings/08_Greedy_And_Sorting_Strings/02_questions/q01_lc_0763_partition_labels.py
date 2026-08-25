"""LeetCode #763 - Partition Labels.
Question Link: https://leetcode.com/problems/partition-labels/
"""
from typing import List


class BruteForce:
    def solve(self, s: str) -> List[int]:
        last = {}
        for i in range(len(s)):
            last[s[i]] = i
        answer = []
        start = 0
        end = 0
        for i in range(len(s)):
            end = max(end, last[s[i]])
            if i == end:
                answer.append(end - start + 1)
                start = i + 1
        return answer


# Complexity (BruteForce / OptimalSolution)
#   Time:  O(n) — record last positions and scan once.
#   Space: O(k) — last index for each distinct character.


class OptimalSolution(BruteForce):
    pass

