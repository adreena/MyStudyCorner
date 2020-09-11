# time O(n+logk)
# space O(n+k)

import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(lambda:0)
        for num in nums:
            count[num]+=1

        heap = []
        for key, val in count.items():
            heapq.heappush(heap, (val,key))
            if len(heap)>k:
                heapq.heappop(heap)
        return [x for _, x in heap]
