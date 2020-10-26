# time O(nlogn)
# space O(n)
import heapq
class Solution:
    def reorganizeString(self, S: str) -> str:
        counts = defaultdict(lambda:0)
        for c in S:
            counts[c]+=1
        heap = []
        for k, v in counts.items():
            if v > (len(S)+1)/2:
                return ''
            heapq.heappush(heap, [-v, k])
        
        output = []
        while len(heap)>=2:
            val1, a = heapq.heappop(heap)
            val2, b = heapq.heappop(heap)
            output.append(a)
            output.append(b)
            val1+=1
            val2+=1
            if val1:
                heapq.heappush(heap,[val1, a])
            if val2:
                heapq.heappush(heap, [val2, b])
        if heap:
            _, c = heap.pop()
            output.append(c)
        return ''.join(output)