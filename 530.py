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
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        minimum_diff = float("infinity")
        vals = []

        def dfs(root):
            nonlocal minimum_diff
            if not root:
                return 0

            dfs(root.left)
            vals.append(root.val)
            dfs(root.right)
        
        dfs(root)

        for i in range(1, len(vals)):
            minimum_diff = min(minimum_diff,vals[i] - vals[i-1])

        return minimum_diff

if __name__ == "__main__":
    solution = Solution()

    root_vals = [1,0,48,None,None,12,49]
    root = createTree(root_vals)

    print(solution.getMinimumDifference(root))