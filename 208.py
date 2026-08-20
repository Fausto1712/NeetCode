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


if __name__ == "__main__":
    words = ["apple", "app", "banana"]
    trie = Trie()

    for word in words:
        trie.insert(word)

    print("Search apple:", trie.search("apple"))
    print("Search app:", trie.search("app"))
    print("Search banana:", trie.search("banana"))
    print("Starts with app:", trie.startsWith("app"))
    print("Starts with ban:", trie.startsWith("ban"))