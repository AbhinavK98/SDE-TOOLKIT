"""LeetCode #76 - Minimum Window Substring.
Question Link: https://leetcode.com/problems/minimum-window-substring/
"""


class BruteForce:
    def solve(self, s: str, t: str) -> str:
        need = self._count(t)
        best = ''
        for i in range(len(s)):
            window = {}
            for j in range(i, len(s)):
                window[s[j]] = window.get(s[j], 0) + 1
                if self._covers(window, need):
                    candidate = s[i:j + 1]
                    if not best or len(candidate) < len(best):
                        best = candidate
                    break
        return best

    def _count(self, text: str) -> dict[str, int]:
        count = {}
        for ch in text:
            count[ch] = count.get(ch, 0) + 1
        return count

    def _covers(self, window: dict[str, int], need: dict[str, int]) -> bool:
        for ch in need:
            if window.get(ch, 0) < need[ch]:
                return False
        return True


# Complexity (BruteForce)
#   Time:  O(n^2*k) — each candidate may compare required characters.
#   Space: O(k) — frequency maps.


class BetterSolution:
    def solve(self, s: str, t: str) -> str:
        if not t:
            return ''
        need = {}
        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        window = {}
        have = 0
        required = len(need)
        left = 0
        best_len = float('inf')
        best_left = 0

        for right in range(len(s)):
            ch = s[right]
            window[ch] = window.get(ch, 0) + 1
            if ch in need and window[ch] == need[ch]:
                have += 1

            while have == required:
                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best_left = left
                left_ch = s[left]
                window[left_ch] -= 1
                if left_ch in need and window[left_ch] < need[left_ch]:
                    have -= 1
                left += 1

        if best_len == float('inf'):
            return ''
        return s[best_left:best_left + best_len]


# Complexity (BetterSolution / OptimalSolution)
#   Time:  O(n + m) — each pointer moves forward at most n times.
#   Space: O(k) — counts for distinct characters.


class OptimalSolution(BetterSolution):
    pass

