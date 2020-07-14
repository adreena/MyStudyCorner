# time: O(logN)
# space: O(N)
import heapq
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.min_heap, -num)
        heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
        if len(self.min_heap)<len(self.max_heap):
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

    def findMedian(self) -> float:
        if len(self.min_heap)==0:
            return None
        if len(self.min_heap) == len(self.max_heap):
            return (-self.min_heap[0]+self.max_heap[0])/2.
        else:
            return -self.min_heap[0]
