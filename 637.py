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
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque()
        second = deque()
        queue.append(root)

        averages = []
        sum = 0
        nums = 1
        while queue:
            curr = queue.popleft()
            if not curr:
                continue

            sum += curr.val

            if curr.left:
                second.append(curr.left)
            if curr.right:
                second.append(curr.right)

            if not queue:
                queue = second
                second = deque()
                averages.append(sum/nums)
                nums = len(queue)
                sum = 0

        return averages

if __name__ == "__main__":
    solution = Solution()

    root_vals = [3,9,20,None,None,15,7]
    root = createTree(root_vals)

    print(solution.averageOfLevels(root))