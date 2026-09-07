"""LeetCode #17 - Letter Combinations of a Phone Number.
Question Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
"""
from typing import List


class BruteForce:
    def solve(self, digits: str) -> List[str]:
        if not digits:
            return []
        mapping = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz',
        }
        answer = []
        self._backtrack(digits, mapping, 0, [], answer)
        return answer

    def _backtrack(self, digits: str, mapping: dict[str, str], index: int, path: list[str], answer: List[str]) -> None:
        if index == len(digits):
            answer.append(''.join(path))
            return
        for ch in mapping[digits[index]]:
            path.append(ch)
            self._backtrack(digits, mapping, index + 1, path, answer)
            path.pop()


# Complexity (BruteForce / OptimalSolution)
#   Time:  O(4^n * n) — generate combinations and join paths.
#   Space: O(n) — recursion path, excluding output.


class OptimalSolution(BruteForce):
    pass

