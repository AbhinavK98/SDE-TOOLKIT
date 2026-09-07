"""LeetCode #209 - Minimum Size Subarray Sum.
Question Link: https://leetcode.com/problems/minimum-size-subarray-sum/
"""
from typing import List


class BruteForce:
    def solve(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        answer = n + 1
        for i in range(n):
            current = 0
            for j in range(i, n):
                current += nums[j]
                if current >= target:
                    length = j - i + 1
                    if length < answer:
                        answer = length
                    break
        if answer == n + 1:
            return 0
        return answer


# Complexity (BruteForce)
#   Time:  O(n^2) worst — every start i, extend j until sum >= target.
#   Space: O(1)   — only running sum and answer tracker.


class BetterSolution:
    def solve(self, target: int, nums: List[int]) -> int:
        left = 0
        window_sum = 0
        best = len(nums) + 1
        n = len(nums)

        for right in range(n):
            window_sum += nums[right]
            while window_sum >= target:
                length = right - left + 1
                if length < best:
                    best = length
                window_sum -= nums[left]
                left += 1

        if best == n + 1:
            return 0
        return best


# Complexity (BetterSolution)
#   Time:  O(n) — delegates to variable sliding window.
#   Space: O(1) — only window pointers and sum.


class OptimalSolution:
    def solve(self, target: int, nums: List[int]) -> int:
        left = 0
        window_sum = 0
        best = len(nums) + 1
        n = len(nums)

        for right in range(n):
            window_sum += nums[right]
            while window_sum >= target:
                length = right - left + 1
                if length < best:
                    best = length
                window_sum -= nums[left]
                left += 1

        if best == n + 1:
            return 0
        return best


# Complexity (OptimalSolution)
#   Time:  O(n) — right expands once; left shrinks at most n times total.
#   Space: O(1) — window sum tracked with two indices.

