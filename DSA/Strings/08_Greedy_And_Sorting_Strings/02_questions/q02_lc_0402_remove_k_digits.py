"""LeetCode #402 - Remove K Digits.
Question Link: https://leetcode.com/problems/remove-k-digits/
"""


class BruteForce:
    def solve(self, num: str, k: int) -> str:
        stack = []
        for digit in num:
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        while k > 0 and stack:
            stack.pop()
            k -= 1
        answer = ''.join(stack).lstrip('0')
        return answer if answer else '0'


# Complexity (BruteForce / OptimalSolution)
#   Time:  O(n) — each digit is pushed and popped at most once.
#   Space: O(n) — stack stores kept digits.


class OptimalSolution(BruteForce):
    pass

