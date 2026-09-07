"""LeetCode #3 - Longest Substring Without Repeating Characters.
Question Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""


class BruteForce:
    def solve(self, s: str) -> int:
        best = 0
        for i in range(len(s)):
            seen = set()
            for j in range(i, len(s)):
                if s[j] in seen:
                    break
                seen.add(s[j])
                best = max(best, j - i + 1)
        return best


# Complexity (BruteForce)
#   Time:  O(n^2) — try every starting point.
#   Space: O(k) — set stores current unique window.


class BetterSolution:
    def solve(self, s: str) -> int:
        last_seen = {}
        left = 0
        best = 0
        for right in range(len(s)):
            ch = s[right]
            if ch in last_seen and last_seen[ch] >= left:
                left = last_seen[ch] + 1
            last_seen[ch] = right
            best = max(best, right - left + 1)
        return best


# Complexity (BetterSolution / OptimalSolution)
#   Time:  O(n) — right scans once and left only jumps forward.
#   Space: O(k) — last seen index per distinct character.


class OptimalSolution(BetterSolution):
    pass

