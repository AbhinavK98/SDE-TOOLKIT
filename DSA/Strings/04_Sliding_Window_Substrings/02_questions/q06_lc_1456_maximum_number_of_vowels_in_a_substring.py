"""LeetCode #1456 - Maximum Number of Vowels in a Substring of Given Length.
Question Link: https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
"""


class BruteForce:
    def solve(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        best = 0
        for i in range(len(s) - k + 1):
            count = 0
            for ch in s[i:i + k]:
                if ch in vowels:
                    count += 1
            best = max(best, count)
        return best


# Complexity (BruteForce)
#   Time:  O(n*k) — count vowels inside every window.
#   Space: O(k) — slicing creates window copy.


class BetterSolution:
    def solve(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        current = 0
        best = 0
        for right in range(len(s)):
            if s[right] in vowels:
                current += 1
            if right >= k and s[right - k] in vowels:
                current -= 1
            if right >= k - 1:
                best = max(best, current)
        return best


# Complexity (BetterSolution / OptimalSolution)
#   Time:  O(n) — one entering and one leaving update per step.
#   Space: O(1) — fixed vowel set.


class OptimalSolution(BetterSolution):
    pass

