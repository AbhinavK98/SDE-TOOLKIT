"""
Question: Contains Duplicate
LeetCode: #217
Question Link: https://leetcode.com/problems/contains-duplicate/
Difficulty: Easy
Pattern: HashMap/HashSet lookup
"""

from typing import List


class BruteForce:
    def solve(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    return True
        return False


# Complexity (BruteForce)
#   Time:  O(n^2) — compares every pair (i, j) for equality.
#   Space: O(1)   — no auxiliary storage beyond loop indices.


class BetterSolution:
    def solve(self, nums: List[int]) -> bool:
        sorted_nums = sorted(nums)
        n = len(sorted_nums)
        for i in range(1, n):
            if sorted_nums[i] == sorted_nums[i - 1]:
                return True
        return False


# Complexity (BetterSolution)
#   Time:  O(n log n) — sorting costs O(n log n); one linear scan for neighbors.
#   Space: O(n)       — sorted copy of the array.


class OptimalSolution:
    def solve(self, nums: List[int]) -> bool:
        seen = set()
        n = len(nums)
        for i in range(n):
            if nums[i] in seen:
                return True
            seen.add(nums[i])
        return False


# Complexity (OptimalSolution)
#   Time:  O(n) — one pass; set membership check is O(1) average.
#   Space: O(n) — set holds up to n distinct values in worst case.


if __name__ == '__main__':
    print(OptimalSolution().solve([1, 2, 3, 1]))

