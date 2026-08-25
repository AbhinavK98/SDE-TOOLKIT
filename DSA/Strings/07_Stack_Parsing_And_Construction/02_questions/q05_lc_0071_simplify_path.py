"""LeetCode #71 - Simplify Path.
Question Link: https://leetcode.com/problems/simplify-path/
"""


class BruteForce:
    def solve(self, path: str) -> str:
        stack = []
        for part in path.split('/'):
            if part == '' or part == '.':
                continue
            if part == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(part)
        return '/' + '/'.join(stack)


# Complexity (BruteForce / OptimalSolution)
#   Time:  O(n) — split and process every path token.
#   Space: O(n) — stack stores valid path parts.


class OptimalSolution(BruteForce):
    pass

