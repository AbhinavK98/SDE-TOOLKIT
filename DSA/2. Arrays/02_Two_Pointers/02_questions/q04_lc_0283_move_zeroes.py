"""LeetCode #283 - Move Zeroes.
Question Link: https://leetcode.com/problems/move-zeroes/
"""
from typing import List


class BruteForce:
    def solve(self, nums: List[int]) -> None:
        non_zero = []
        n = len(nums)
        for i in range(n):
            if nums[i] != 0:
                non_zero.append(nums[i])
        zero_count = n - len(non_zero)
        for i in range(len(non_zero)):
            nums[i] = non_zero[i]
        for i in range(len(non_zero), n):
            nums[i] = 0


# Complexity (BruteForce)
#   Time:  O(n) — filter pass + rebuild array.
#   Space: O(n) — `non_zero` list and zero padding.


class BetterSolution:
    def solve(self, nums: List[int]) -> None:
        write = 0
        n = len(nums)
        for read in range(n):
            if nums[read] != 0:
                nums[write], nums[read] = nums[read], nums[write]
                write += 1


# Complexity (BetterSolution / OptimalSolution)
#   Time:  O(n) — read visits each index once; swaps are O(1).
#   Space: O(1) — in-place swap; no extra array.


class OptimalSolution(BetterSolution):
    pass

