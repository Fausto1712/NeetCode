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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        hasIt = False

        def dfs(root, currSum):
            nonlocal hasIt

            if not root:
                return 0
            
            currSum += root.val

            if currSum == targetSum and not root.left and not root.right:
                hasIt = True

            dfs(root.left, currSum)
            dfs(root.right, currSum)

        dfs(root, 0)

        return hasIt
        


if __name__ == "__main__":
    solution = Solution()

    root_vals = [5,4,8,11,None,13,4,7,2,None,None,None,1]
    targetSum = 22
    root = createTree(root_vals)

    print(solution.hasPathSum(root, targetSum))