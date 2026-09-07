"""LeetCode #205 - Isomorphic Strings.
Question Link: https://leetcode.com/problems/isomorphic-strings/
"""


class BruteForce:
    def solve(self, s: str, t: str) -> bool:
        return self._pattern(s) == self._pattern(t)

    def _pattern(self, text: str) -> list[int]:
        seen = {}
        pattern = []
        for ch in text:
            if ch not in seen:
                seen[ch] = len(seen)
            pattern.append(seen[ch])
        return pattern


# Complexity (BruteForce)
#   Time:  O(n) — build normalized pattern for both strings.
#   Space: O(n) — pattern arrays store n ids.


class BetterSolution:
    def solve(self, s: str, t: str) -> bool:
        s_to_t = {}
        t_to_s = {}
        for a, b in zip(s, t):
            if a in s_to_t and s_to_t[a] != b:
                return False
            if b in t_to_s and t_to_s[b] != a:
                return False
            s_to_t[a] = b
            t_to_s[b] = a
        return True


# Complexity (BetterSolution / OptimalSolution)
#   Time:  O(n) — each aligned pair is processed once.
#   Space: O(k) — maps store distinct characters.


class OptimalSolution(BetterSolution):
    pass

