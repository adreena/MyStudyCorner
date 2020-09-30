# time O(NW)
# space O(N)

class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        cards = defaultdict(lambda:0)
        for h in hand:
            cards[h]+=1
        
        sorted_keys = sorted(hand)
        for k in sorted_keys:
            if cards[k]>0:
                cards[k]-=1
                for j in range(1,W):
                    if k+j not in cards or cards[k+j]==0:
                        return False
                    cards[k+j]-=1
        for k, v in cards.items():
            if v != 0 :
                return False
        return True