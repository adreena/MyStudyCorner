# time: O(n)
# space: O(1)

def oddEvenList(self, head: ListNode) -> ListNode:
    prev_node = None
    count = 0
    last_odd_node = None
    itr = head
    while itr :
        node = itr
        if count%2 == 0:
            if prev_node:
                prev_node.next = node.next
            prev_node = node
            itr = prev_node.next
            if last_odd_node:
                node.next = last_odd_node.next
                last_odd_node.next = node
            last_odd_node = node
        else:   
            prev_node = node
            itr = prev_node.next
        count+=1
    return head