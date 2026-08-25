"""LeetCode #792 - Number of Matching Subsequences.
Question Link: https://leetcode.com/problems/number-of-matching-subsequences/
"""
from collections import defaultdict, deque
from typing import List


class BruteForce:
    def solve(self, s: str, words: List[str]) -> int:
        count = 0
        for word in words:
            if self._is_subsequence(word, s):
                count += 1
        return count

    def _is_subsequence(self, word: str, s: str) -> bool:
        i = 0
        for ch in s:
            if i < len(word) and word[i] == ch:
                i += 1
        return i == len(word)


# Complexity (BruteForce)
#   Time:  O(words * len(s)) — scan s for each word.
#   Space: O(1) — pointer state only.


class BetterSolution:
    def solve(self, s: str, words: List[str]) -> int:
        waiting = defaultdict(deque)
        for word in words:
            waiting[word[0]].append((word, 0))
        matched = 0
        for ch in s:
            queue = waiting[ch]
            for _ in range(len(queue)):
                word, index = queue.popleft()
                index += 1
                if index == len(word):
                    matched += 1
                else:
                    waiting[word[index]].append((word, index))
        return matched


# Complexity (BetterSolution / OptimalSolution)
#   Time:  O(len(s) + total word characters) — each waiting state advances once.
#   Space: O(words) — queues store active word states.


class OptimalSolution(BetterSolution):
    pass

