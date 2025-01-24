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

def printTree(root, level=0, prefix="Root: "):
    if root is not None:
        print(" " * (level * 4) + prefix + str(root.val))
        if root.left or root.right:
            if root.left:
                printTree(root.left, level + 1, "L--- ")
            else:
                print(" " * ((level + 1) * 4) + "L--- None")
            if root.right:
                printTree(root.right, level + 1, "R--- ")
            else:
                print(" " * ((level + 1) * 4) + "R--- None")


class Solution:
    def lowestCommonAncestorMyOwn(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root
        path = []
        while curr and curr.val != p.val:
            path.append(curr)
            if curr.val > p.val:
                curr = curr.left
            else:
                curr = curr.right
        path.append(curr)

        curr = root
        path2 = []
        while curr and curr.val != q.val:
            path2.append(curr)
            if curr.val > q.val:
                curr = curr.left
            else:
                curr = curr.right
        path2.append(curr)

        set_path = set(path)
        set_path2 = set(path2)
        common_steps = set_path & set_path2
        lowestCommonAncestor = None
        for step in (path if len(path) <= len(path2) else path2):
                if step in common_steps:
                    lowestCommonAncestor = step
                else:
                    break
        return lowestCommonAncestor
    
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root

        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur

if __name__ == "__main__":
    solution = Solution()
    
    root_vals = [6,2,8,0,4,7,9,None,None,3,5]
    p = TreeNode(2)
    q = TreeNode(8)
    root = createTree(root_vals)
    print(solution.lowestCommonAncestorMyOwn(root, p, q).val)
