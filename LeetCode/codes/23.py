#time O(NLogk)
# space O(1)

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        if len(lists) == 0 or not lists:
            return None
        
        def merge2(l1, l2):
            head=itr = ListNode(-1)
            while l1 and l2:
                if l1.val<=l2.val:
                    itr.next = l1
                    l1 = l1.next
                else:
                    itr.next = l2
                    l2 = l1
                    l1 = itr.next.next
                itr = itr.next
            if l1:
                itr.next = l1
            elif l2:
                itr.next = l2
                
            return head.next
        
        a = lists.pop(0)
        while lists:
            b = lists.pop(0)
            a = merge2(a,b)
            
        return a