"""LeetCode #724 - Find Pivot Index.
Question Link: https://leetcode.com/problems/find-pivot-index/
"""
from typing import List


class BruteForce:
    def solve(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if sum(nums[:i]) == sum(nums[i + 1:]):
                return i
        return -1


# Complexity (BruteForce)
#   Time:  O(n^2) — for each pivot i, rescan left and right halves.
#   Space: O(1)   — only index and temporary slice sums.


class BetterSolution:
    def solve(self, nums: List[int]) -> int:
        prefix = [0]
        n = len(nums)
        for i in range(n):
            prefix.append(prefix[-1] + nums[i])

        for i in range(n):
            left_sum = prefix[i]
            right_sum = prefix[-1] - prefix[i + 1]
            if left_sum == right_sum:
                return i
        return -1


# Complexity (BetterSolution)
#   Time:  O(n) build prefix + O(n) scan = O(n) total.
#   Space: O(n) — prefix array of length n + 1.


class OptimalSolution:
    def solve(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum = 0
        n = len(nums)
        for i in range(n):
            right_sum = total - left_sum - nums[i]
            if left_sum == right_sum:
                return i
            left_sum += nums[i]
        return -1


# Complexity (OptimalSolution)
#   Time:  O(n) — one total sum + single pass updating left_sum.
#   Space: O(1) — right_sum derived as total - left_sum - nums[i].
