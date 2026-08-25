"""LeetCode #767 - Reorganize String.
Question Link: https://leetcode.com/problems/reorganize-string/
"""
import heapq


class BruteForce:
    def solve(self, s: str) -> str:
        count = {}
        for ch in s:
            count[ch] = count.get(ch, 0) + 1
        heap = [(-freq, ch) for ch, freq in count.items()]
        heapq.heapify(heap)
        previous_freq = 0
        previous_ch = ''
        answer = []

        while heap or previous_freq < 0:
            if not heap:
                return ''
            freq, ch = heapq.heappop(heap)
            answer.append(ch)
            freq += 1
            if previous_freq < 0:
                heapq.heappush(heap, (previous_freq, previous_ch))
            previous_freq, previous_ch = freq, ch
        return ''.join(answer)


# Complexity (BruteForce / OptimalSolution)
#   Time:  O(n log k) — heap operation per character.
#   Space: O(k) — heap stores distinct characters.


class OptimalSolution(BruteForce):
    pass

