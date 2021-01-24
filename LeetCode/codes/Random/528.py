# time O(logn) +O(n)
# space: O(N)
import random
class Solution:

    def __init__(self, w: List[int]):
        
        self.prefix_sum = w
        for i in range(1, len(w)):
            self.prefix_sum[i]+=self.prefix_sum[i-1]
        self.sum = self.prefix_sum[-1]

    def pickIndex(self) -> int:
        seed = random.randint(1,self.sum)
        left =0
        right = len(self.prefix_sum)-1
        while left <= right:
            mid = (left+right) //2
            if seed <= self.prefix_sum[mid]:
                right = mid-1
            else:
                left = mid+1
        return left