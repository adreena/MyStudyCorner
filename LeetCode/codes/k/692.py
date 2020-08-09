
# time:O(nlogn)
# space: O(n)

import heapq  
from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts= Counter(words)
        heap = []
        for word, count in counts.items():
            heapq.heappush(heap, [-counts[word], word])
        output = []
        while heap and len(output)<k:
            c, w = heapq.heappop(heap)
            output.append(w)
        return output
        