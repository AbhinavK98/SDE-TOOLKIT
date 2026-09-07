"""LeetCode #125 - Valid Palindrome.
Question Link: https://leetcode.com/problems/valid-palindrome/
"""


class BruteForce:
    def solve(self, s: str) -> bool:
        cleaned = []
        for ch in s:
            if ch.isalnum():
                cleaned.append(ch.lower())
        return cleaned == cleaned[::-1]


# Complexity (BruteForce)
#   Time:  O(n) — scan and reverse cleaned characters.
#   Space: O(n) — cleaned list stores valid characters.


class BetterSolution:
    def solve(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True


# Complexity (BetterSolution / OptimalSolution)
#   Time:  O(n) — each pointer moves inward at most n steps total.
#   Space: O(1) — no cleaned copy.


class OptimalSolution(BetterSolution):
    pass

