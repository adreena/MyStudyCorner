
# time: O(N)
# space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        def merge(l1, l2):
            itr = head = ListNode(-1)
            while l1 and l2:
                if l1.val <= l2.val:
                    itr.next = l1
                    l1 = l1.next
                else:
                    itr.next = l2
                    l2 = l1
                    l1 = itr.next.next
                itr = itr.next
            if l1:
                itr.next = l1
            if l2:
                itr.next = l2
            return head.next
        if len(lists)==0:
            return None
        keep = lists.pop(0)
        while lists:
            nxt = lists.pop()
            keep = merge(keep, nxt)
        return keep