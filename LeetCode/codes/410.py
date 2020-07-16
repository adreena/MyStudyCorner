# time: O(n log(sum))
# space: O(n)

def splitArray(self, nums: List[int], m: int) -> int:

    right = sum(nums)
    left = max(nums)
    max_sum = right
    while left<= right:
        mid = (left+right)//2
        total = 0
        parts = 1
        for i in range(len(nums)):
            if total+nums[i]>mid:
                parts+=1
                total = 0
            total+=nums[i]

        if parts <= m:
            right = mid-1
            max_sum = min(max_sum, mid)
        else:
            left = mid+1
    return max_sum
