"""LeetCode #227 - Basic Calculator II.
Question Link: https://leetcode.com/problems/basic-calculator-ii/
"""


class BruteForce:
    def solve(self, s: str) -> int:
        stack = []
        number = 0
        operation = '+'
        for i in range(len(s)):
            ch = s[i]
            if ch.isdigit():
                number = number * 10 + int(ch)
            if (not ch.isdigit() and ch != ' ') or i == len(s) - 1:
                if operation == '+':
                    stack.append(number)
                elif operation == '-':
                    stack.append(-number)
                elif operation == '*':
                    stack.append(stack.pop() * number)
                else:
                    stack.append(int(stack.pop() / number))
                operation = ch
                number = 0
        return sum(stack)


# Complexity (BruteForce / OptimalSolution)
#   Time:  O(n) — parse expression once.
#   Space: O(n) — stack stores signed terms.


class OptimalSolution(BruteForce):
    pass

