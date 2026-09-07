"""
Question: Two Sum
LeetCode: #1
Question Link: https://leetcode.com/problems/two-sum/
Difficulty: Easy
Pattern: HashMap Complement

Problem Statement:
Given an integer array and a target, return indices of two numbers such that
those two numbers add up to target.

Why this pattern:
For each number x, we need (target - x). A hash map lets us answer
"Have we seen this needed value?" in O(1) average time.
"""

from typing import List


class BruteForce:
    """Check every pair using nested loops."""

    def solve(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []


# Complexity (BruteForce)
#   Time:  O(n^2) — outer loop fixes index i, inner loop checks every j > i.
#   Space: O(1)   — only loop counters; no extra structure grows with n.


class BetterSolution:
    """Sort copy + two pointers (keeps original indices separately)."""

    def solve(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        indexed = []
        for i in range(n):
            indexed.append((nums[i], i))
        indexed.sort()

        left = 0
        right = n - 1
        while left < right:
            current_sum = indexed[left][0] + indexed[right][0]
            if current_sum == target:
                return [indexed[left][1], indexed[right][1]]
            if current_sum < target:
                left += 1
            else:
                right -= 1
        return []


# Complexity (BetterSolution)
#   Time:  O(n log n) — sorting dominates; two-pointer scan is O(n).
#   Space: O(n)       — indexed copy stores (value, index) pairs.


class OptimalSolution:
    """One-pass hash map complement lookup."""

    def solve(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]
            if complement in seen:
                return [seen[complement], i]
            seen[nums[i]] = i

        return []


# Complexity (OptimalSolution)
#   Time:  O(n) — single pass; each hash map lookup/insert is O(1) average.
#   Space: O(n) — map stores up to n values seen so far.


if __name__ == '__main__':
    print(OptimalSolution().solve([2, 7, 11, 15], 9))

