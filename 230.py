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
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        smallestK = []

        def dfs(root):
            if not root:
                return None
            nonlocal smallestK
            dfs(root.left)
            smallestK.append(root.val)
            dfs(root.right)
        
        dfs(root)
        
        return smallestK[k-1]

if __name__ == "__main__":
    solution = Solution()

    root_vals = [3,1,4,None,2]
    root =  createTree(root_vals)

    print(f"The smallest kth element is {solution.kthSmallest(root, 1)}")