"""LeetCode #1047 - Remove All Adjacent Duplicates In String.
Question Link: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
"""


class BruteForce:
    def solve(self, s: str) -> str:
        changed = True
        while changed:
            changed = False
            answer = []
            i = 0
            while i < len(s):
                if i + 1 < len(s) and s[i] == s[i + 1]:
                    changed = True
                    i += 2
                else:
                    answer.append(s[i])
                    i += 1
            s = ''.join(answer)
        return s


# Complexity (BruteForce)
#   Time:  O(n^2) — repeated passes may remove only one pair.
#   Space: O(n) — rebuilt string each pass.


class BetterSolution:
    def solve(self, s: str) -> str:
        stack = []
        for ch in s:
            if stack and stack[-1] == ch:
                stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)


# Complexity (BetterSolution / OptimalSolution)
#   Time:  O(n) — each character is pushed or popped once.
#   Space: O(n) — stack stores remaining characters.


class OptimalSolution(BetterSolution):
    pass

