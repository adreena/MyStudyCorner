# time O(N)
# space O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        itr = ListNode(-1)
        head = itr
        while l1 and l2:
            if l1.val<=l2.val:
                itr.next = l1
                l1 = l1.next
            else:
                itr.next = l2
                l2 = l1
                l1=itr.next.next
            itr = itr.next
        if l1:
            itr.next = l1
        if l2:
            itr.next = l2
        return head.next