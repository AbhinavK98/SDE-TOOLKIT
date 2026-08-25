"""LeetCode #212 - Word Search II.
Question Link: https://leetcode.com/problems/word-search-ii/
"""
from typing import List


class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.word = None


class BruteForce:
    def solve(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = word

        answer = []
        rows = len(board)
        cols = len(board[0]) if rows else 0
        for row in range(rows):
            for col in range(cols):
                self._dfs(board, row, col, root, answer)
        return answer

    def _dfs(self, board: List[List[str]], row: int, col: int, node: TrieNode, answer: List[str]) -> None:
        if row < 0 or col < 0 or row == len(board) or col == len(board[0]):
            return
        ch = board[row][col]
        if ch == '#' or ch not in node.children:
            return

        next_node = node.children[ch]
        if next_node.word is not None:
            answer.append(next_node.word)
            next_node.word = None

        board[row][col] = '#'
        self._dfs(board, row + 1, col, next_node, answer)
        self._dfs(board, row - 1, col, next_node, answer)
        self._dfs(board, row, col + 1, next_node, answer)
        self._dfs(board, row, col - 1, next_node, answer)
        board[row][col] = ch


# Complexity (BruteForce / OptimalSolution)
#   Time:  O(rows*cols*4^L) worst case — trie prunes invalid prefixes.
#   Space: O(total word characters) — trie plus recursion depth.


class OptimalSolution(BruteForce):
    pass

