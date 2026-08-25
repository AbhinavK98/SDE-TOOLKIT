"""LeetCode #438 - Find All Anagrams in a String.
Question Link: https://leetcode.com/problems/find-all-anagrams-in-a-string/
"""
from typing import List


class BruteForce:
    def solve(self, s: str, p: str) -> List[int]:
        target = sorted(p)
        k = len(p)
        answer = []
        for i in range(len(s) - k + 1):
            if sorted(s[i:i + k]) == target:
                answer.append(i)
        return answer


# Complexity (BruteForce)
#   Time:  O(n*k log k) — sort every candidate window.
#   Space: O(k) — sorted window copy.


class BetterSolution:
    def solve(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        need = [0] * 26
        window = [0] * 26
        for ch in p:
            need[ord(ch) - ord('a')] += 1
        answer = []
        k = len(p)
        for right in range(len(s)):
            window[ord(s[right]) - ord('a')] += 1
            if right >= k:
                window[ord(s[right - k]) - ord('a')] -= 1
            if window == need:
                answer.append(right - k + 1)
        return answer


# Complexity (BetterSolution / OptimalSolution)
#   Time:  O(26*n) — compare fixed-size count arrays.
#   Space: O(1) — fixed alphabet counts, excluding answer.


class OptimalSolution(BetterSolution):
    pass

