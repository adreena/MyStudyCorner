# time O(Nk)
# space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def reverse(node):
            h = ListNode(-1)
            h.next = node
            while node and node.next:
                temp = node.next
                node.next = node.next.next
                temp.next = h.next
                h.next = temp
            return h.next, node
        count = 0
        prev_node = None
        new_head = ListNode(-1)
        new_head.next = head
        cur_head = head
        node = head
        while node:
            count+=1
            if count == k:
                temp = node.next
                node.next = None
                h, t = reverse(cur_head)
                t.next = temp
                if prev_node:
                    prev_node.next = h
                else:
                    new_head.next = h
                prev_node = t
                cur_head = t.next
                count = 0
                node = t

            node = node.next
        return new_head.next
