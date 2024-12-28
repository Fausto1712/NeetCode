class Node:
    def __init__(self,x: int, next: 'Node' = None, random: 'Node' =  None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: Node) -> Node:
        newHead = Node(0)
        newCurr, curr = newHead, head
        nodeSet = {}
        while curr:
            newCurr.next = Node(curr.val)
            nodeSet[curr] = newCurr.next
            newCurr = newCurr.next
            curr = curr.next

        newCurr, curr = newHead.next, head
        while curr:
            if curr.random:
                newCurr.random = nodeSet[curr.random]
            newCurr = newCurr.next
            curr = curr.next

        return newHead.next

head = [[7,None],[13,0],[11,4],[10,2],[1,0]]

print("")
print(f'Result {Solution.copyRandomList(Solution,head)}')
print("")