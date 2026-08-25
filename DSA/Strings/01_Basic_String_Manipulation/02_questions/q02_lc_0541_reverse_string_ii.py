"""LeetCode #541 - Reverse String II.
Question Link: https://leetcode.com/problems/reverse-string-ii/
"""


class BruteForce:
    def solve(self, s: str, k: int) -> str:
        answer = []
        n = len(s)
        for start in range(0, n, 2 * k):
            answer.append(s[start:start + k][::-1])
            answer.append(s[start + k:start + 2 * k])
        return ''.join(answer)


# Complexity (BruteForce)
#   Time:  O(n) — every character is copied into output once.
#   Space: O(n) — output chunks store the result.


class BetterSolution:
    def solve(self, s: str, k: int) -> str:
        chars = list(s)
        n = len(chars)
        for start in range(0, n, 2 * k):
            left = start
            right = min(start + k - 1, n - 1)
            while left < right:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1
        return ''.join(chars)


# Complexity (BetterSolution / OptimalSolution)
#   Time:  O(n) — each character belongs to at most one reversed block.
#   Space: O(n) — Python strings are immutable, so a char list is needed.


class OptimalSolution(BetterSolution):
    pass

