"""LeetCode #93 - Restore IP Addresses.
Question Link: https://leetcode.com/problems/restore-ip-addresses/
"""
from typing import List


class BruteForce:
    def solve(self, s: str) -> List[str]:
        answer = []
        self._backtrack(s, 0, [], answer)
        return answer

    def _backtrack(self, s: str, index: int, parts: list[str], answer: List[str]) -> None:
        if len(parts) == 4:
            if index == len(s):
                answer.append('.'.join(parts))
            return
        for length in range(1, 4):
            if index + length > len(s):
                break
            part = s[index:index + length]
            if self._valid(part):
                parts.append(part)
                self._backtrack(s, index + length, parts, answer)
                parts.pop()

    def _valid(self, part: str) -> bool:
        if len(part) > 1 and part[0] == '0':
            return False
        return int(part) <= 255


# Complexity (BruteForce / OptimalSolution)
#   Time:  O(1) — at most 3^4 segment choices.
#   Space: O(1) — at most 4 path parts.


class OptimalSolution(BruteForce):
    pass

