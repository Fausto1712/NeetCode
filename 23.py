from typing import List

class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next


class Solution:
    def mergeKListsIteration(self,lists: List[ListNode]) ->ListNode:
        if not lists:
            return None

        headSet = {}
        for i in range(len(lists)):
            if lists[i]:
                headSet[i] = lists[i]

        newHead = curr = ListNode(0)

        while headSet:
            min_key = min(headSet, key=lambda key: headSet[key].val)
            curr.next = headSet[min_key]
            curr = curr.next
            headSet[min_key] = headSet[min_key].next
            if not headSet[min_key]:
                del headSet[min_key]

        return newHead.next
    
    def mergeKListsDivideAndConquer(self, lists: List[ListNode]) -> ListNode:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergeList(l1, l2))
            lists = mergedLists
        return lists[0]

    def mergeList(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next