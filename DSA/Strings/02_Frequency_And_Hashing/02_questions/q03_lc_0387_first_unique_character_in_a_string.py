"""LeetCode #387 - First Unique Character in a String.
Question Link: https://leetcode.com/problems/first-unique-character-in-a-string/
"""


class BruteForce:
    def solve(self, s: str) -> int:
        n = len(s)
        for i in range(n):
            repeated = False
            for j in range(n):
                if i != j and s[i] == s[j]:
                    repeated = True
                    break
            if not repeated:
                return i
        return -1


# Complexity (BruteForce)
#   Time:  O(n^2) — each character may compare with all others.
#   Space: O(1) — only loop variables.


class BetterSolution:
    def solve(self, s: str) -> int:
        count = {}
        for ch in s:
            count[ch] = count.get(ch, 0) + 1
        for i in range(len(s)):
            if count[s[i]] == 1:
                return i
        return -1


# Complexity (BetterSolution / OptimalSolution)
#   Time:  O(n) — count pass plus original-order scan.
#   Space: O(k) — k distinct characters.


class OptimalSolution(BetterSolution):
    pass

