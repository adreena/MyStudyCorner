# time O(logn)
# space O(N)

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        compute_sum = lambda x: sum([ceil(n/x) for n in nums])
        i = 1
        j = nums[-1]
        while i<=j:
            mid = (i+j)//2
            c = compute_sum(mid)
            if c <=threshold:
                j = mid-1
            else:
                i= mid+1
        return i