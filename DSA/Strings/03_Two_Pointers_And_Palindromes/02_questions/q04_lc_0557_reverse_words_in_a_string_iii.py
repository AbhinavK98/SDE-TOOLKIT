"""LeetCode #557 - Reverse Words in a String III.
Question Link: https://leetcode.com/problems/reverse-words-in-a-string-iii/
"""


class BruteForce:
    def solve(self, s: str) -> str:
        return ' '.join(word[::-1] for word in s.split(' '))


# Complexity (BruteForce)
#   Time:  O(n) — reverse each word and join.
#   Space: O(n) — stores reversed words and output.


class BetterSolution:
    def solve(self, s: str) -> str:
        chars = list(s)
        start = 0
        n = len(chars)
        for i in range(n + 1):
            if i == n or chars[i] == ' ':
                self._reverse(chars, start, i - 1)
                start = i + 1
        return ''.join(chars)

    def _reverse(self, chars: list[str], left: int, right: int) -> None:
        while left < right:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1


# Complexity (BetterSolution / OptimalSolution)
#   Time:  O(n) — each character is reversed inside exactly one word.
#   Space: O(n) — char list is needed for Python string mutation.


class OptimalSolution(BetterSolution):
    pass

