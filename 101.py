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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        leftqueue = deque()
        leftqueue.append(root.left)

        rightqueue = deque()
        rightqueue.append(root.right)

        isSymmetric = True

        if not root or (not root.left and not root.right):
            return isSymmetric
        
        while leftqueue and rightqueue:
            leftcurr = leftqueue.popleft()
            rightcurr = rightqueue.popleft()

            if ((leftcurr or rightcurr) and not (leftcurr and rightcurr)) or (leftcurr.val != rightcurr.val):
                isSymmetric = False
                return False
            
            if leftcurr.left and rightcurr.right:
                leftqueue.append(leftcurr.left)
                rightqueue.append(rightcurr.right)

            elif (leftcurr.left or rightcurr.right) and not (leftcurr.left and rightcurr.right):
                isSymmetric = False
                return False
            
            if leftcurr.right and rightcurr.left:
                leftqueue.append(leftcurr.right)
                rightqueue.append(rightcurr.left)

            elif (leftcurr.right or rightcurr.left) and not (leftcurr.right and rightcurr.left):
                isSymmetric = False
                return False
        
        return isSymmetric

    def isSymmetric2(self, root: Optional[TreeNode]) -> bool:
        def is_mirror(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
            if not left and not right:
                return True
            if not left or not right or left.val != right.val:
                return False
            return is_mirror(left.left, right.right) and is_mirror(left.right, right.left)

        return is_mirror(root.left, root.right) if root else True


if __name__ == "__main__":
    solution = Solution()

    root_vals = [1,0]
    root = createTree(root_vals)

    print(solution.isSymmetric(root))
    print(solution.isSymmetric2(root))