"""LeetCode #383 - Ransom Note.
Question Link: https://leetcode.com/problems/ransom-note/
"""


class BruteForce:
    def solve(self, ransomNote: str, magazine: str) -> bool:
        magazine_chars = list(magazine)
        for ch in ransomNote:
            if ch not in magazine_chars:
                return False
            magazine_chars.remove(ch)
        return True


# Complexity (BruteForce)
#   Time:  O(n*m) — list search/remove can scan magazine characters repeatedly.
#   Space: O(m) — mutable copy of magazine.


class BetterSolution:
    def solve(self, ransomNote: str, magazine: str) -> bool:
        count = {}
        for ch in magazine:
            count[ch] = count.get(ch, 0) + 1
        for ch in ransomNote:
            if count.get(ch, 0) == 0:
                return False
            count[ch] -= 1
        return True


# Complexity (BetterSolution / OptimalSolution)
#   Time:  O(n + m) — count magazine, consume ransom note.
#   Space: O(k) — k distinct magazine characters.


class OptimalSolution(BetterSolution):
    pass

