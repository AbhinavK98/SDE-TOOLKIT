"""LeetCode #680 - Valid Palindrome II.
Question Link: https://leetcode.com/problems/valid-palindrome-ii/
"""


class BruteForce:
    def solve(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        for i in range(len(s)):
            candidate = s[:i] + s[i + 1:]
            if candidate == candidate[::-1]:
                return True
        return False


# Complexity (BruteForce)
#   Time:  O(n^2) — build and check a candidate after each deletion.
#   Space: O(n) — candidate strings are created.


class BetterSolution:
    def solve(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return self._is_palindrome(s, left + 1, right) or self._is_palindrome(s, left, right - 1)
            left += 1
            right -= 1
        return True

    def _is_palindrome(self, s: str, left: int, right: int) -> bool:
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True


# Complexity (BetterSolution / OptimalSolution)
#   Time:  O(n) — at most two extra linear checks after first mismatch.
#   Space: O(1) — pointer checks only.


class OptimalSolution(BetterSolution):
    pass

