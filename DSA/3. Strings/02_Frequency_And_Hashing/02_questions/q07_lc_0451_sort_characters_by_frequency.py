"""LeetCode #451 - Sort Characters By Frequency.
Question Link: https://leetcode.com/problems/sort-characters-by-frequency/
"""


class BruteForce:
    def solve(self, s: str) -> str:
        return ''.join(sorted(s, key=lambda ch: (-s.count(ch), ch)))


# Complexity (BruteForce)
#   Time:  O(n^2 log n) — count inside sort key repeatedly scans the string.
#   Space: O(n) — sorted output copy.


class BetterSolution:
    def solve(self, s: str) -> str:
        count = {}
        for ch in s:
            count[ch] = count.get(ch, 0) + 1
        chars = sorted(count.keys(), key=lambda ch: count[ch], reverse=True)
        answer = []
        for ch in chars:
            answer.append(ch * count[ch])
        return ''.join(answer)


# Complexity (BetterSolution / OptimalSolution)
#   Time:  O(n + k log k) — count chars, sort distinct chars.
#   Space: O(n + k) — counts and output pieces.


class OptimalSolution(BetterSolution):
    pass

