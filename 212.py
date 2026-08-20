from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for word in words:
            curr = root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.is_word = True

        rows, cols = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        result: List[str] = []

        def dfs(r: int, c: int, node: TrieNode, path: str) -> None:
            if not (0 <= r < rows and 0 <= c < cols):
                return

            char = board[r][c]
            if char == "#":
                return

            next_node = node.children.get(char)
            if next_node is None:
                return

            board[r][c] = "#"
            path += char

            if next_node.is_word:
                result.append(path)
                next_node.is_word = False

            for dr, dc in directions:
                dfs(r + dr, c + dc, next_node, path)

            board[r][c] = char

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")

        return result


if __name__ == "__main__":
    solution = Solution()
    board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
    words = ["oath","pea","eat","rain"]
    result = solution.findWords(board, words)
    print(f"Board: {board}")
    print(f"Words: {words}")
    print(f"Result: {result}")