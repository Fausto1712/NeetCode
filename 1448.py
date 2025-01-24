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
    def goodNodes(self, root: TreeNode) -> int:
        goodNodes = 0

        def dfs(root, maxNodeVal):
            if not root:
                return 0
            
            nonlocal goodNodes
            if root.val >= maxNodeVal:
                goodNodes += 1
                maxNodeVal = root.val

            dfs(root.left, maxNodeVal)
            dfs(root.right, maxNodeVal)
            
        dfs(root, root.val)
        return goodNodes

if __name__ == "__main__":
    solution = Solution()

    root_vals = [3,1,4,3,None,1,5]
    root =  createTree(root_vals)

    print(solution.goodNodes(root))
