"""LeetCode #424 - Longest Repeating Character Replacement.
Question Link: https://leetcode.com/problems/longest-repeating-character-replacement/
"""


class BruteForce:
    def solve(self, s: str, k: int) -> int:
        best = 0
        for i in range(len(s)):
            count = {}
            max_freq = 0
            for j in range(i, len(s)):
                count[s[j]] = count.get(s[j], 0) + 1
                max_freq = max(max_freq, count[s[j]])
                if j - i + 1 - max_freq <= k:
                    best = max(best, j - i + 1)
        return best


# Complexity (BruteForce)
#   Time:  O(n^2) — extend every starting index.
#   Space: O(k) — frequency map for current substring.


class BetterSolution:
    def solve(self, s: str, k: int) -> int:
        count = {}
        left = 0
        max_freq = 0
        best = 0
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            max_freq = max(max_freq, count[s[right]])
            while right - left + 1 - max_freq > k:
                count[s[left]] -= 1
                left += 1
            best = max(best, right - left + 1)
        return best


# Complexity (BetterSolution / OptimalSolution)
#   Time:  O(n) — each pointer moves forward.
#   Space: O(k) — counts distinct characters in window.


class OptimalSolution(BetterSolution):
    pass

