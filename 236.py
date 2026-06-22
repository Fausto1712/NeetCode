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
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pathA = []
        pathB = []

        def dfs(root, currPath):
            nonlocal pathA
            nonlocal pathB

            if not root:
                return

            currPath.append(root)
            if root is q:
                pathA = currPath.copy()
            if root is p:
                pathB = currPath.copy()

            dfs(root.left, currPath)
            dfs(root.right, currPath)
            currPath.pop()
            
        dfs(root, [])

        if not pathA or not pathB:
            return None

        min_len = min(len(pathA), len(pathB))
        i = 0
        while i < min_len and pathA[i] is pathB[i]:
            i += 1

        return pathA[i-1]

if __name__ == "__main__":
    solution = Solution()

    root_vals = [3,5,1,6,2,0,8,None,None,7,4]
    # inputs may be ints (values) or TreeNode objects; normalize below
    p_input = 5
    q_input = 1
    root = createTree(root_vals)

    def find(node, val):
        if not node:
            return None
        if node.val == val:
            return node
        left = find(node.left, val)
        if left:
            return left
        return find(node.right, val)

    def ensure_node(node_or_val):
        if isinstance(node_or_val, TreeNode):
            return node_or_val
        return find(root, node_or_val)

    p_node = ensure_node(p_input)
    q_node = ensure_node(q_input)

    ans = solution.lowestCommonAncestor(root, p_node, q_node)
    print(ans.val if ans else None)