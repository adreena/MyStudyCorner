class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(start, end):
            rand = random.randint(start,end)
            pivot = end
            nums[pivot], nums[rand] = nums[rand], nums[pivot]
            
            write_idx = start
            for i in range(start,end):
                if nums[i]>=nums[pivot]:
                    nums[i], nums[write_idx] = nums[write_idx], nums[i]
                    write_idx+=1
            nums[write_idx], nums[pivot] = nums[pivot], nums[write_idx]
            return write_idx
        
        k-=1
        if k>len(nums):
            return None
        
        start, end = 0 , len(nums)-1
        while start<=end:
            p = partition(start,end)
            if p==k:
                return nums[p]
            elif p>k:
                end = p-1
            else:
                start = p+1
        