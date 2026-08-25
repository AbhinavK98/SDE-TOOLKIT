"""LeetCode #1358 - Number of Substrings Containing All Three Characters.
Question Link: https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/
"""


class BruteForce:
    def solve(self, s: str) -> int:
        total = 0
        n = len(s)
        for i in range(n):
            seen = set()
            for j in range(i, n):
                seen.add(s[j])
                if len(seen) == 3:
                    total += n - j
                    break
        return total


# Complexity (BruteForce)
#   Time:  O(n^2) — try each starting index.
#   Space: O(1) — only characters a, b, c.


class BetterSolution:
    def solve(self, s: str) -> int:
        count = {'a': 0, 'b': 0, 'c': 0}
        left = 0
        total = 0
        for right in range(len(s)):
            count[s[right]] += 1
            while count['a'] and count['b'] and count['c']:
                total += len(s) - right
                count[s[left]] -= 1
                left += 1
        return total


# Complexity (BetterSolution / OptimalSolution)
#   Time:  O(n) — left and right each move forward.
#   Space: O(1) — fixed count map.


class OptimalSolution(BetterSolution):
    pass

