class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        head = current = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        return head

            
list1 = [1,2,4]
list2 = [1,3,4]

print()
print(f"Max sliding window: {Solution.mergeTwoLists(Solution, list1, list2)}")
print()

