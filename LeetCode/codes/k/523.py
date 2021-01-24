# time O(N)
# space O(N)
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        rem= {0:-1}
        cur_sum = 0
        for i in range(len(nums)):
            cur_sum+=nums[i]
            if k!=0:
                cur_sum %= k
            if cur_sum in rem:
                if i - rem[cur_sum]>1:
                    return True
            else:
                rem[cur_sum]=i
        return False