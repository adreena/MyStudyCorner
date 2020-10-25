# time: O(N)
# space O(1) characters are limited 28

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        word_maps= defaultdict(lambda:set())
        in_deg = defaultdict(lambda:0)
        chars = set()
        for w in words:
            for c in w:
                chars.add(c)
                in_deg[c] = 0
                
        for w1, w2 in zip(words, words[1:]):
            match = True
            for c1, c2 in zip(w1,w2):
                if c1!=c2:
                    if c2 not in word_maps[c1]:
                        in_deg[c2]+=1
                    word_maps[c1].add(c2)
                    match=False
                    break
            if match and len(w2)<len(w1):
                return ""
                    
                    
        starts = []
        for c in chars:
            if in_deg[c]==0:
                starts.append(c)
                
        output = []
        while starts:
            top = starts.pop(0)
            output.append(top)
            for nxt in word_maps[top]:
                in_deg[nxt]-=1
                if in_deg[nxt] == 0:
                    starts.append(nxt)
        if len(output) != len(chars):
            return ""
        return ''.join(output)
        