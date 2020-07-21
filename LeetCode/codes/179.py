# time O(nlogn)
# space: O(n)

import heapq
class Node:
    def __init__(self, val):
        self.val = val
    def __lt__(self, other):
        o1 = int(self.val+other.val)
        o2 = int(other.val+self.val)
        return o1 >o2
    
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [Node(str(num)) for num in nums]
        groups = defaultdict(lambda:[])
        for num in nums:
            heapq.heappush(groups[int(num.val[0])], num)

        if len(groups)==1 and 0 in list(groups.keys()):
            return "0"
        
        output = ""
        for i in range(9, -1, -1):
            while groups[i]:
                x = heapq.heappop(groups[i]).val
                output+=x
        return output