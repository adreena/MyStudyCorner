
# time O(n)
# space O(1)

from bisect import bisect_left
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        f = float('inf')
        s = float('inf')
        for num in nums:
            if num<=f:
                f = num
            elif num<=s:
                s = num
            else:
                return True
        return False
        

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        lis = []
        for num in nums:
            idx = bisect_left(lis, num)
            if idx == len(lis):
                lis.append(num)
            else:
                lis[idx] = num
            if len(lis)==3:
                return True
        return False