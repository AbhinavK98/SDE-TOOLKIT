"""LeetCode #179 - Largest Number.
Question Link: https://leetcode.com/problems/largest-number/
"""
from functools import cmp_to_key
from typing import List


class BruteForce:
    def solve(self, nums: List[int]) -> str:
        values = [str(num) for num in nums]
        values.sort(key=cmp_to_key(self._compare))
        answer = ''.join(values)
        return '0' if answer[0] == '0' else answer

    def _compare(self, a: str, b: str) -> int:
        if a + b > b + a:
            return -1
        if a + b < b + a:
            return 1
        return 0


# Complexity (BruteForce / OptimalSolution)
#   Time:  O(n log n * m) — custom comparison joins strings of length m.
#   Space: O(n*m) — string values and sorted output.


class OptimalSolution(BruteForce):
    pass

