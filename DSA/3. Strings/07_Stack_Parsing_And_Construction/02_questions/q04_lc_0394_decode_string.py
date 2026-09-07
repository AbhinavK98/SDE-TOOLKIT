"""LeetCode #394 - Decode String.
Question Link: https://leetcode.com/problems/decode-string/
"""


class BruteForce:
    def solve(self, s: str) -> str:
        stack = []
        current = ''
        number = 0
        for ch in s:
            if ch.isdigit():
                number = number * 10 + int(ch)
            elif ch == '[':
                stack.append((current, number))
                current = ''
                number = 0
            elif ch == ']':
                previous, repeat = stack.pop()
                current = previous + current * repeat
            else:
                current += ch
        return current


# Complexity (BruteForce / OptimalSolution)
#   Time:  O(output length) — decoded characters must be produced.
#   Space: O(output length) — stack and current decoded text.


class OptimalSolution(BruteForce):
    pass

