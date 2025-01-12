class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        isEqual = True

        def dfs(p: TreeNode, q: TreeNode):
            nonlocal isEqual
            if not p and not q:
                return 0
            elif not p or not q:
                isEqual = False
                return 0
            if p != q:
                isEqual = False
                return 0
            left = dfs(p.left, q.left)
            right = dfs(p.right, q.right)
            return left + right

        dfs(p,q)

        return isEqual