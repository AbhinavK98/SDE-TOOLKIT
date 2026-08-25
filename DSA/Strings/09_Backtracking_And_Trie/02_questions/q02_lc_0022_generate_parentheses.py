"""LeetCode #22 - Generate Parentheses.
Question Link: https://leetcode.com/problems/generate-parentheses/
"""
from typing import List


class BruteForce:
    def solve(self, n: int) -> List[str]:
        answer = []
        self._backtrack(n, 0, 0, [], answer)
        return answer

    def _backtrack(self, n: int, open_count: int, close_count: int, path: list[str], answer: List[str]) -> None:
        if len(path) == 2 * n:
            answer.append(''.join(path))
            return
        if open_count < n:
            path.append('(')
            self._backtrack(n, open_count + 1, close_count, path, answer)
            path.pop()
        if close_count < open_count:
            path.append(')')
            self._backtrack(n, open_count, close_count + 1, path, answer)
            path.pop()


# Complexity (BruteForce / OptimalSolution)
#   Time:  O(Cn*n) — generate Catalan number of valid strings.
#   Space: O(n) — recursion path, excluding output.


class OptimalSolution(BruteForce):
    pass

