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
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        solutions = []
        def dfs(root, currSum, currPath):
            nonlocal solutions

            if not root:
                return 0
            
            currSum += root.val
            currPath.append(root.val)

            if currSum == targetSum and not root.left and not root.right:
                solutions.append(currPath.copy())

            dfs(root.left, currSum, currPath.copy())
            dfs(root.right, currSum, currPath.copy())
        
        dfs(root, 0, [])

        return solutions
        


if __name__ == "__main__":
    solution = Solution()

    root_vals = [5,4,8,11,None,13,4,7,2,None,None,5,1]
    targetSum = 22
    root = createTree(root_vals)

    print(solution.pathSum(root, targetSum))