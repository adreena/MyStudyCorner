# time: O(nlogn)
# space: O(n)

from collections import defaultdict

def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
    sorted_nums = sorted(nums)
    counts = defaultdict(lambda:0)
    smaller = defaultdict(lambda:0)
    for i in range(len(sorted_nums)):
        if i>0 and sorted_nums[i] != sorted_nums[i-1]:
            smaller[sorted_nums[i]] = counts[sorted_nums[i-1]] + smaller[sorted_nums[i-1]]
        counts[sorted_nums[i]]+=1
    
    return [smaller[num] for num in nums]
        
        