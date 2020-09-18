# time O(logk)
# space O(k)
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for n in nums:
            heapq.heappush(heap, n)
            if len(heap)>k:
                heapq.heappop(heap)
        if len(heap) == 0:
            return -1
        return heap[0]
