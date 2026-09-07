"""LeetCode #791 - Custom Sort String.
Question Link: https://leetcode.com/problems/custom-sort-string/
"""


class BruteForce:
    def solve(self, order: str, s: str) -> str:
        rank = {ch: i for i, ch in enumerate(order)}
        return ''.join(sorted(s, key=lambda ch: rank.get(ch, len(order))))


# Complexity (BruteForce)
#   Time:  O(n log n) — sorting characters by custom rank.
#   Space: O(n) — sorted output.


class BetterSolution:
    def solve(self, order: str, s: str) -> str:
        count = {}
        for ch in s:
            count[ch] = count.get(ch, 0) + 1
        answer = []
        for ch in order:
            if ch in count:
                answer.append(ch * count.pop(ch))
        for ch, freq in count.items():
            answer.append(ch * freq)
        return ''.join(answer)


# Complexity (BetterSolution / OptimalSolution)
#   Time:  O(n + k) — count s and emit ordered characters.
#   Space: O(n + k) — count map and output pieces.


class OptimalSolution(BetterSolution):
    pass

