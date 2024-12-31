class ListNode:
    def __init__(self,x = 0):
        self.val = x
        self.next = None

class Solution:
    def hasCycleHash(self,head: ListNode) -> bool:
        nodeSet = {}
        curr = head
        while curr:
            if curr in nodeSet and nodeSet[curr]:
               return True
            nodeSet[curr] = True
            curr =  curr.next
        return False
    
    def hasCycleTwoPointers(self,head: ListNode) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


def create_list(values):
    dummy = ListNode()
    curr = dummy
    for val in values:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def print_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(" -> ".join(map(str, result)))

head = create_list([3,2,0,-4])
print("Original List:")
print_list(head)

solution = Solution()
result1 = solution.hasCycleHash(head)
result2 = solution.hasCycleTwoPointers(head)

print(f'Result 1: {result1}')
print(f'Result 2: {result2}')
