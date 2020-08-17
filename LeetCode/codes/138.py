# time O(N)
# space O(N)

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        self.cache = defaultdict(lambda:None)
        def copy(node):
            if node is None:
                return None
            if node in self.cache:
                return self.cache[node]
            new_node = Node(node.val)
            self.cache[node] = new_node
            new_node.next = copy(node.next)
            new_node.random = copy(node.random)
            return new_node
        return copy(head)
            