class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        isBalanced = True

        def dfs(root: TreeNode):
            if not root:
                return 0
            nonlocal isBalanced
            left = dfs(root.left)
            right = dfs(root.right)

            if not (left == right or left == right + 1 or left == right - 1):
                isBalanced = False

            return 1 + max(left,right)
        dfs(root)

        return isBalanced