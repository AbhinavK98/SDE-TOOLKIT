"""LeetCode #977 - Squares of a Sorted Array.
Question Link: https://leetcode.com/problems/squares-of-a-sorted-array/
"""
from typing import List


class BruteForce:
    def solve(self, nums: List[int]) -> List[int]:
        n = len(nums)
        squares = []
        for i in range(n):
            squares.append(nums[i] * nums[i])
        squares.sort()
        return squares


# Complexity (BruteForce)
#   Time:  O(n log n) — square each value then sort.
#   Space: O(n)       — generator materialized by sorted().


class BetterSolution:
    def solve(self, nums: List[int]) -> List[int]:
        negatives = []
        non_negatives = []
        n = len(nums)
        for i in range(n):
            square = nums[i] * nums[i]
            if nums[i] < 0:
                negatives.append(square)
            else:
                non_negatives.append(square)

        # negatives were squared in order; reverse so largest comes first
        reversed_negatives = []
        for i in range(len(negatives) - 1, -1, -1):
            reversed_negatives.append(negatives[i])

        merged = []
        i = 0
        j = 0
        while i < len(reversed_negatives) and j < len(non_negatives):
            if reversed_negatives[i] <= non_negatives[j]:
                merged.append(reversed_negatives[i])
                i += 1
            else:
                merged.append(non_negatives[j])
                j += 1
        while i < len(reversed_negatives):
            merged.append(reversed_negatives[i])
            i += 1
        while j < len(non_negatives):
            merged.append(non_negatives[j])
            j += 1
        return merged


# Complexity (BetterSolution)
#   Time:  O(n) — split, reverse negatives, merge like merge-sort.
#   Space: O(n) — separate negative/non-negative squared lists + merged output.


class OptimalSolution:
    def solve(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [0] * n
        left, right = 0, n - 1
        write = n - 1

        while left <= right:
            left_square = nums[left] * nums[left]
            right_square = nums[right] * nums[right]
            if left_square > right_square:
                answer[write] = left_square
                left += 1
            else:
                answer[write] = right_square
                right -= 1
            write -= 1
        return answer


# Complexity (OptimalSolution)
#   Time:  O(n) — two pointers from ends; each index written once.
#   Space: O(n) — output array (required by problem; no sorting needed).

