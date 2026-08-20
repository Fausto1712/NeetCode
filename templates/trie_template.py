from __future__ import annotations
from typing import List

# Trie template for problems like Implement Trie
# Input example: words = ["apple", "app", "banana"]


class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        curr = self.root

        for c in word:
            if c in curr.children:
                curr = curr.children[c]
            else:
                return False
        return curr.endOfWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for c in prefix:
            if c in curr.children:
                curr = curr.children[c]
            else:
                return False

        return True


class Solution:
    def solveTrie(self, words: List[str]) -> dict:
        trie = Trie()
        for word in words:
            trie.insert(word)

        return {
            "words": words,
            "search": {
                "apple": trie.search("apple"),
                "app": trie.search("app"),
                "banana": trie.search("banana"),
                "appl": trie.search("appl"),
            },
            "prefix": {
                "app": trie.startsWith("app"),
                "ban": trie.startsWith("ban"),
                "appl": trie.startsWith("appl"),
            },
        }


if __name__ == "__main__":
    words = ["apple", "app", "banana"]

    solution = Solution()
    result = solution.solveTrie(words)

    print("Input words:", result["words"])
    print("Search results:", result["search"])
    print("Prefix checks:", result["prefix"])
