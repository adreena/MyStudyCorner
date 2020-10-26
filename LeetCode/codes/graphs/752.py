# time O(N*D^N)
# space O(D^N)

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        visited = set()
        def get_next(combo):
            for i in range(4):
                for d in [-1,1]:
                    c = str((int(combo[i])+d)%10)
                    temp = combo[:i]+str(c)+combo[i+1:]
                    yield temp
                    
        q = [('0000',0)]
        while q:
            combo, count = q.pop(0)
            visited.add(combo)
            if combo == target:
                return count
            if combo in deadends:
                continue
            for nxt in get_next(combo):
                if nxt not in deadends and nxt not in visited:
                    q.append([nxt, count+1])
                    visited.add(nxt)
            
                        
        return -1