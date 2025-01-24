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
    def isValidBST(self, root: TreeNode) -> bool:
        isValid = True

        def dfs(root, min, max):
            if not root:
                return 0
            nonlocal isValid
            if root.val >= max or root.val <= min:
                isValid = False
            dfs(root.left, min, root.val)
            dfs(root.right,root.val, max)

        dfs(root, float("-infinity"), float("infinity"))
        return isValid


if __name__ == "__main__":
    solution = Solution()

    root_vals = [2,1,3]
    root =  createTree(root_vals)

    print(f"The tree is {"valid" if solution.isValidBST(root) else "not valid"}")
