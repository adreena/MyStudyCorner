# time O(N)
# space:O(N)

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_idx = {c:i for i , c in enumerate(order)}
        found = False
        for w1, w2 in zip(words, words[1:]):
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    if order_idx[c1]>order_idx[c2]:
                        return False
                    found = True
                    break
            if not found and len(w1)>len(w2):
                return False
        return True