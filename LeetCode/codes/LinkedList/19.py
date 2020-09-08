#time O(N)
#space: O(1)

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        nth = ListNode(-1)
        nth.next = head
        prev_node= None
        count = 0
        node = head
        while node:
            node = node.next
            count+=1
            if count == n:
                temp = nth
                nth = nth.next
                if nth != head:
                    prev_node = temp
                count-=1
        if prev_node:
            prev_node.next = nth.next
        else:
            head = head.next
        
        return head