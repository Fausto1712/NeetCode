class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        curr = head
        count = 0
        while l1 or l2 or count != 0:
            valL1 = l1.val if l1 and hasattr(l1, 'val') else 0
            valL2 = l2.val if l2 and hasattr(l2, 'val') else 0
                
            curr.next = ListNode((valL1 + valL2 + count) % 10)
            if 1 <= (count + valL1 + valL2)/10:
                count = 1
            else:
                count = 0
            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return head.next

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

l1 = create_list([2,4,3])
l2 = create_list([5,6,4])
print("Original Lists:")
print_list(l1)
print_list(l2)

solution = Solution()
result = solution.addTwoNumbers(l1,l2)

print("Result:")
print_list(result)