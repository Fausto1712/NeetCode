class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    def serialize(self, root):
        if not root:
            return []
        data = [root.val]
        queue = [root]
        while queue:
            curr = queue.pop(0)
            if curr.left:
                queue.append(curr.left)
                data.append(curr.left.val)
            else:
                data.append(None)

            if curr.right:
                queue.append(curr.right)
                data.append(curr.right.val)
            else:
                data.append(None)
        return data
        

    def deserialize(self, data):
        def createTree(vals, idx=0):
            if idx >= len(vals) or vals[idx] is None:
                return None
            root = TreeNode(vals[idx])
            root.left = createTree(vals, 2 * idx + 1)
            root.right = createTree(vals, 2 * idx + 2)
            return root
        
        return createTree(data)
    
    # Encodes a tree to a single string.
    def serializeDFS(self, root: TreeNode) -> str:
        res = []

        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserializeDFS(self, data: str) -> TreeNode:
        vals = data.split(",")
        self.i = 0

        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()

if __name__ == "__main__":
    codec = Codec()
    data = []
    tree = codec.deserialize(data)
    data = codec.serialize(tree)
    tree = codec.deserialize(data)
    data = codec.serialize(tree)
    