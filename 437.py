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
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        numPaths = 0

        def count_from(node, currSum):
            nonlocal numPaths
            if not node:
                return

            currSum += node.val
            if currSum == targetSum:
                numPaths += 1

            count_from(node.left, currSum)
            count_from(node.right, currSum)

        def dfs(node):
            if not node:
                return

            count_from(node, 0)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return numPaths


def pathSum_prefix(root: Optional[TreeNode], targetSum: int) -> int:
    count = 0
    prefix = {0: 1}

    def dfs(node, currSum):
        nonlocal count
        if not node:
            return

        currSum += node.val
        count += prefix.get(currSum - targetSum, 0)
        prefix[currSum] = prefix.get(currSum, 0) + 1

        dfs(node.left, currSum)
        dfs(node.right, currSum)

        prefix[currSum] -= 1

    dfs(root, 0)
    return count


if __name__ == "__main__":
    solution = Solution()

    root_vals = [10,5,-3,3,2,None,11,3,-2,None,1]
    root = createTree(root_vals)
    targetSum = 8

    print(solution.pathSum(root, targetSum))
    print(pathSum_prefix(root, targetSum))