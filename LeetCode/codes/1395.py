# time :O(n2)
# space: O(1)

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        
        n = len(rating)
        count = 0
        for cur in range(n):
            ll, lg = 0, 0
            rl, rg = 0, 0
            for left in range(0, cur):
                if rating[left]<rating[cur]:
                    ll+=1
                elif rating[left]>rating[cur]:
                    lg+=1
            
            for right in range(cur+1, n):
                if rating[right]>rating[cur]:
                    rg+=1
                elif rating[right]<rating[cur]:
                    rl+=1
            count+= ll*rg + lg*rl
        
        return count