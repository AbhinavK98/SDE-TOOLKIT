"""LeetCode #1647 - Minimum Deletions to Make Character Frequencies Unique.
Question Link: https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/
"""


class BruteForce:
    def solve(self, s: str) -> int:
        count = {}
        for ch in s:
            count[ch] = count.get(ch, 0) + 1
        used = set()
        deletions = 0
        for freq in count.values():
            while freq > 0 and freq in used:
                freq -= 1
                deletions += 1
            if freq > 0:
                used.add(freq)
        return deletions


# Complexity (BruteForce / OptimalSolution)
#   Time:  O(n + k^2) worst case — frequencies may be decremented repeatedly.
#   Space: O(k) — used frequencies and character counts.


class OptimalSolution(BruteForce):
    pass

