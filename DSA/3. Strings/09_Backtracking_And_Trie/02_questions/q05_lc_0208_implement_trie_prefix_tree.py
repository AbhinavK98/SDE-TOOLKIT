"""LeetCode #208 - Implement Trie (Prefix Tree).
Question Link: https://leetcode.com/problems/implement-trie-prefix-tree/
"""


class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.is_word = False


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_word = True

    def search(self, word: str) -> bool:
        node = self._find_node(word)
        return node is not None and node.is_word

    def startsWith(self, prefix: str) -> bool:
        return self._find_node(prefix) is not None

    def _find_node(self, text: str) -> TrieNode | None:
        node = self.root
        for ch in text:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node


# Complexity
#   insert Time: O(n), Space: O(n) new nodes in worst case.
#   search Time: O(n), Space: O(1).
#   startsWith Time: O(n), Space: O(1).


class OptimalSolution(Trie):
    pass

