"""LeetCode #643 - Maximum Average Subarray I.
Question Link: https://leetcode.com/problems/maximum-average-subarray-i/
"""
from typing import List


class BruteForce:
    def solve(self, nums: List[int], k: int) -> float:
        n = len(nums)
        best = None
        for i in range(n - k + 1):
            window_sum = 0
            for j in range(i, i + k):
                window_sum += nums[j]
            if best is None or window_sum > best:
                best = window_sum
        return best / k


# Complexity (BruteForce)
#   Time:  O(n * k) — each window of size k recomputes sum from scratch.
#   Space: O(1)   — only loop indices and best tracker.


class BetterSolution:
    def solve(self, nums: List[int], k: int) -> float:
        n = len(nums)
        window_sum = 0
        for i in range(k):
            window_sum += nums[i]
        best_sum = window_sum

        for right in range(k, n):
            window_sum += nums[right]
            window_sum -= nums[right - k]
            if window_sum > best_sum:
                best_sum = window_sum

        return best_sum / k


# Complexity (BetterSolution)
#   Time:  O(n) — delegates to fixed-size sliding window.
#   Space: O(1) — incremental window sum update.


class OptimalSolution:
    def solve(self, nums: List[int], k: int) -> float:
        n = len(nums)
        window_sum = 0
        for i in range(k):
            window_sum += nums[i]
        best_sum = window_sum

        for right in range(k, n):
            window_sum += nums[right]
            window_sum -= nums[right - k]
            if window_sum > best_sum:
                best_sum = window_sum

        return best_sum / k


# Complexity (OptimalSolution)
#   Time:  O(n) — add new right element, drop left in O(1) per step.
#   Space: O(1) — fixed window of size k rolled across array.

