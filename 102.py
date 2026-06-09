from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def createTree(vals, idx=0):
    if idx >= len(vals) or vals[idx] is None:
        return None
    root = TreeNode(vals[idx])
    root.left = createTree(vals, 2 * idx + 1)
    root.right = createTree(vals, 2 * idx + 2)

    return root

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = [[]]
        queue = deque()
        queue.append(root)
        second = deque()
        i = 0
        if not root:
            return []

        while queue:
            curr = queue.popleft()

            if not curr:
                continue

            levels[i].append(curr.val)

            if curr.left:
                second.append(curr.left)
            if curr.right:
                second.append(curr.right)

            if not queue and second:
                i += 1
                queue = second
                second = deque()
                levels.append([])

        return levels

    def levelOrder2(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            level = []

            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(level)

        return result


if __name__ == "__main__":
    solution = Solution()

    root_vals = [3,9,20,None,None,15,7]
    root = createTree(root_vals)

    print(solution.levelOrder(root))
    print(solution.levelOrder2(root))