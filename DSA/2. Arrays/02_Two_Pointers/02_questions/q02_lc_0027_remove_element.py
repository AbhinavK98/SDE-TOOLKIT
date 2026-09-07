"""LeetCode #27 - Remove Element.
Question Link: https://leetcode.com/problems/remove-element/
"""
from typing import List


class BruteForce:
    def solve(self, nums: List[int], val: int) -> int:
        kept = []
        n = len(nums)
        for i in range(n):
            if nums[i] != val:
                kept.append(nums[i])
        for i in range(len(kept)):
            nums[i] = kept[i]
        return len(kept)


# Complexity (BruteForce)
#   Time:  O(n) — list comprehension scans all elements once.
#   Space: O(n) — new list `kept` stores up to n elements.


class BetterSolution:
    def solve(self, nums: List[int], val: int) -> int:
        write = 0
        n = len(nums)
        for read in range(n):
            if nums[read] != val:
                nums[write] = nums[read]
                write += 1
        return write


# Complexity (BetterSolution / OptimalSolution)
#   Time:  O(n) — single read pointer; each element visited once.
#   Space: O(1) — in-place compaction without auxiliary list.


class OptimalSolution(BetterSolution):
    pass

