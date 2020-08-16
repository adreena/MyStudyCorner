
# time:O(nlogn)
# space: O(n)

from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts= Counter(words)
        output = [[-count, word] for word, count in counts.items()]
        return [c for _, c in sorted(output)][:k]
        
        