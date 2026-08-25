"""LeetCode #567 - Permutation in String.
Question Link: https://leetcode.com/problems/permutation-in-string/
"""


class BruteForce:
    def solve(self, s1: str, s2: str) -> bool:
        target = sorted(s1)
        k = len(s1)
        for i in range(len(s2) - k + 1):
            if sorted(s2[i:i + k]) == target:
                return True
        return False


# Complexity (BruteForce)
#   Time:  O(n*k log k) — sort every length-k substring.
#   Space: O(k) — substring/sorted copies.


class BetterSolution:
    def solve(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        need = [0] * 26
        window = [0] * 26
        for ch in s1:
            need[ord(ch) - ord('a')] += 1
        k = len(s1)
        for right in range(len(s2)):
            window[ord(s2[right]) - ord('a')] += 1
            if right >= k:
                window[ord(s2[right - k]) - ord('a')] -= 1
            if window == need:
                return True
        return False


# Complexity (BetterSolution / OptimalSolution)
#   Time:  O(26*n) — fixed alphabet comparison for each window.
#   Space: O(1) — two arrays of size 26.


class OptimalSolution(BetterSolution):
    pass

