"""LeetCode #5 - Longest Palindromic Substring.
Question Link: https://leetcode.com/problems/longest-palindromic-substring/
"""


class BruteForce:
    def solve(self, s: str) -> str:
        best = ''
        n = len(s)
        for i in range(n):
            for j in range(i, n):
                candidate = s[i:j + 1]
                if len(candidate) > len(best) and candidate == candidate[::-1]:
                    best = candidate
        return best


# Complexity (BruteForce)
#   Time:  O(n^3) — O(n^2) substrings and O(n) palindrome checks.
#   Space: O(n) — candidate slicing.


class BetterSolution:
    def solve(self, s: str) -> str:
        best_left = 0
        best_right = 0
        for center in range(len(s)):
            left, right = self._expand(s, center, center)
            if right - left > best_right - best_left:
                best_left, best_right = left, right
            left, right = self._expand(s, center, center + 1)
            if right - left > best_right - best_left:
                best_left, best_right = left, right
        return s[best_left:best_right + 1]

    def _expand(self, s: str, left: int, right: int) -> tuple[int, int]:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1


# Complexity (BetterSolution / OptimalSolution)
#   Time:  O(n^2) — expand around 2n centers.
#   Space: O(1) — only boundaries are stored.


class OptimalSolution(BetterSolution):
    pass

