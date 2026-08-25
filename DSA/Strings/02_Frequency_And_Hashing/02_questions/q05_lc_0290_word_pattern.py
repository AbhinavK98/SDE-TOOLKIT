"""LeetCode #290 - Word Pattern.
Question Link: https://leetcode.com/problems/word-pattern/
"""


class BruteForce:
    def solve(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        return self._ids(list(pattern)) == self._ids(words)

    def _ids(self, values: list[str]) -> list[int]:
        seen = {}
        answer = []
        for value in values:
            if value not in seen:
                seen[value] = len(seen)
            answer.append(seen[value])
        return answer


# Complexity (BruteForce)
#   Time:  O(n) — normalize pattern and words.
#   Space: O(n) — ids and split words.


class BetterSolution:
    def solve(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        char_to_word = {}
        word_to_char = {}
        for ch, word in zip(pattern, words):
            if ch in char_to_word and char_to_word[ch] != word:
                return False
            if word in word_to_char and word_to_char[word] != ch:
                return False
            char_to_word[ch] = word
            word_to_char[word] = ch
        return True


# Complexity (BetterSolution / OptimalSolution)
#   Time:  O(n) — process every pattern/word pair once.
#   Space: O(n) — maps and split words.


class OptimalSolution(BetterSolution):
    pass

