"""LeetCode #242 - Valid Anagram.
Question Link: https://leetcode.com/problems/valid-anagram/
"""


class BruteForce:
    def solve(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


# Complexity (BruteForce)
#   Time:  O(n log n) — sorting both strings dominates.
#   Space: O(n) — sorted copies are created.


class BetterSolution:
    def solve(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = {}
        for ch in s:
            count[ch] = count.get(ch, 0) + 1
        for ch in t:
            if ch not in count:
                return False
            count[ch] -= 1
            if count[ch] < 0:
                return False
        return True


# Complexity (BetterSolution / OptimalSolution)
#   Time:  O(n) — each character is counted once.
#   Space: O(k) — k distinct characters.


class OptimalSolution(BetterSolution):
    pass

