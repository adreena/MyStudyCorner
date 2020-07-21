from collections import defaultdict, Counter
def isPossibleDivide(self, nums: List[int], k: int) -> bool:
    if len(nums)%k!=0:
        return False
    i = 0
    count = 0 
    counter = Counter(nums)
    nums = sorted(list(counter.keys()))
    for num in nums:
        if counter[num]>0:
            match_count = counter[num]
            for i in range(1,k):
                if counter[num+i]<match_count:
                    return False
                counter[num+i]-=match_count
        
    return True