"""LeetCode #345 - Reverse Vowels of a String.
Question Link: https://leetcode.com/problems/reverse-vowels-of-a-string/
"""


class BruteForce:
    def solve(self, s: str) -> str:
        vowels = [ch for ch in s if ch in 'aeiouAEIOU']
        answer = []
        for ch in s:
            if ch in 'aeiouAEIOU':
                answer.append(vowels.pop())
            else:
                answer.append(ch)
        return ''.join(answer)


# Complexity (BruteForce)
#   Time:  O(n) — collect vowels and rebuild string.
#   Space: O(n) — stores vowels and answer.


class BetterSolution:
    def solve(self, s: str) -> str:
        chars = list(s)
        vowels = set('aeiouAEIOU')
        left, right = 0, len(chars) - 1
        while left < right:
            while left < right and chars[left] not in vowels:
                left += 1
            while left < right and chars[right] not in vowels:
                right -= 1
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1
        return ''.join(chars)


# Complexity (BetterSolution / OptimalSolution)
#   Time:  O(n) — pointers scan each character at most once.
#   Space: O(n) — char list for immutable Python string.


class OptimalSolution(BetterSolution):
    pass

