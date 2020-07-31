# time: O(1)
# space: O(N)


from collections import defaultdict

class DNode:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None
        

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.head = DNode(-1, -1)
        self.tail = DNode(-1, -1)
        self.data = defaultdict(lambda:None)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def add(self, key, val):
        new_node = DNode(key, val)
        self.data[key] = new_node
        temp = self.head.next
        new_node.next = temp
        temp.prev = new_node
        new_node.prev = self.head
        self.head.next = new_node
        
        self.size += 1
        
    def remove(self, key):
        node = self.data[key]
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
        del self.data[key]
        self.size-=1
        
    def get(self, key: int) -> int:
        if key in self.data:
            val = self.data[key].val
            self.remove(key)
            self.add(key,val)
            return val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.data:
            self.remove(key)
        elif self.size == self.capacity:
            old_node = self.tail.prev
            self.remove(old_node.key)
        self.add(key,value)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)