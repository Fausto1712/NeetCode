from __future__ import annotations
from collections import deque
from typing import List, Optional

# Binary tree template for LeetCode-style tree problems
# Input example: values = [1, 2, 3, None, None, 4, 5]

class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"TreeNode({self.val})"


def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()
        if values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root


def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    if not root:
        return []

    result: List[Optional[int]] = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    while result and result[-1] is None:
        result.pop()
    return result


class Solution:
    def solveTree(self, root: Optional[TreeNode]) -> int:
        # Replace this stub with your tree solution.
        return 0


if __name__ == "__main__":
    values = [1, 2, 3, None, None, 4, 5]
    root = build_tree(values)

    solution = Solution()
    result = solution.solveTree(root)

    print("Tree input:", values)
    print("Tree level order:", tree_to_list(root))
    print("Result:", result)
