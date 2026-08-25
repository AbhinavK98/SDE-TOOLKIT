"""LeetCode #151 - Reverse Words in a String.
Question Link: https://leetcode.com/problems/reverse-words-in-a-string/
"""


class BruteForce:
    def solve(self, s: str) -> str:
        words = s.split()
        words.reverse()
        return ' '.join(words)


# Complexity (BruteForce)
#   Time:  O(n) — split and join scan all characters.
#   Space: O(n) — words and output store the normalized string.


class BetterSolution:
    def solve(self, s: str) -> str:
        words = []
        i = 0
        n = len(s)
        while i < n:
            while i < n and s[i] == ' ':
                i += 1
            start = i
            while i < n and s[i] != ' ':
                i += 1
            if start < i:
                words.append(s[start:i])
        return ' '.join(reversed(words))


# Complexity (BetterSolution / OptimalSolution)
#   Time:  O(n) — one scan to collect words, one join.
#   Space: O(n) — stores words and output.


class OptimalSolution(BetterSolution):
    pass

