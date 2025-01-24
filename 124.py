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
    def maxPathSum(self, root: TreeNode) -> int:
        res = root.val

        def dfs(root):
            if not root:
                return 0
            
            nonlocal res
            left = max(dfs(root.left),0)
            right = max(dfs(root.right),0)
            res = max(res, left + right + root.val)

            return(max(left, right) + root.val)
        
        dfs(root)
        return res

if __name__ == "__main__":
    solution = Solution()

    root_vals = [-10,9,20,None,None,15,7]
    root =  createTree(root_vals)

    print(f"The max path sum is: {solution.maxPathSum(root)}")