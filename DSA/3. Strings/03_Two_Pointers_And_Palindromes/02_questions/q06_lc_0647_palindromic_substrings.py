"""LeetCode #647 - Palindromic Substrings.
Question Link: https://leetcode.com/problems/palindromic-substrings/
"""


class BruteForce:
    def solve(self, s: str) -> int:
        count = 0
        n = len(s)
        for i in range(n):
            for j in range(i, n):
                candidate = s[i:j + 1]
                if candidate == candidate[::-1]:
                    count += 1
        return count


# Complexity (BruteForce)
#   Time:  O(n^3) — every substring check can take linear time.
#   Space: O(n) — slicing creates candidate strings.


class BetterSolution:
    def solve(self, s: str) -> int:
        total = 0
        for center in range(len(s)):
            total += self._count_from_center(s, center, center)
            total += self._count_from_center(s, center, center + 1)
        return total

    def _count_from_center(self, s: str, left: int, right: int) -> int:
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        return count


# Complexity (BetterSolution / OptimalSolution)
#   Time:  O(n^2) — each center expands while characters match.
#   Space: O(1) — only counters and pointers.


class OptimalSolution(BetterSolution):
    pass

