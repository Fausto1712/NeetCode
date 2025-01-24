from typing import List

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
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
    def rightSideView(self, root: TreeNode) -> List[int]:
        rightSideVals = []

        def dfs(root, depth):
            if not root:
                return None
            if depth == len(rightSideVals):
                rightSideVals.append(root.val)
            
            dfs(root.right, depth+1)
            dfs(root.left, depth+1)

        dfs(root, 0)
        return rightSideVals


if __name__ == "__main__":
    solution = Solution()

    root_vals = [1,2,3,4,None,None,None,5]
    root =  createTree(root_vals)

    print(solution.rightSideView(root))

