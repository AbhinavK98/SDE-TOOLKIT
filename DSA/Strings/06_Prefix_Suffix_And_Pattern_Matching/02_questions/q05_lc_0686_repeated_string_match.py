"""LeetCode #686 - Repeated String Match.
Question Link: https://leetcode.com/problems/repeated-string-match/
"""


class BruteForce:
    def solve(self, a: str, b: str) -> int:
        repeated = a
        count = 1
        while len(repeated) < len(b) + len(a):
            if b in repeated:
                return count
            repeated += a
            count += 1
        return count if b in repeated else -1


# Complexity (BruteForce / OptimalSolution)
#   Time:  O((n + m) * m) average — repeated substring checks over growing text.
#   Space: O(n + m) — repeated string.


class OptimalSolution(BruteForce):
    pass

