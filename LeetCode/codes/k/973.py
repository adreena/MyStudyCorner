
# time: O(nlogk)
# space: O(k)

import heapq
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            dist = sqrt(x**2 + y**2)
            heapq.heappush(heap, (-dist, [x,y]))
            if len(heap)>K:
                heapq.heappop(heap)
        output = []
        while heap:
            d, point = heapq.heappop(heap)
            output.append(point)
        return output