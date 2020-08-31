# time: O(N)
# space O(1) characters are limited 28

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        succ= {}
        in_degree = {}
        chars = set()
        for word in words:
            for c in word:
                succ[c] = set()
                in_degree[c] = 0
                chars.add(c)
        
        for pair in zip(words, words[1:]):
            for a,b in zip(*pair):
                if a!=b:
                    if b not in succ[a]:
                        in_degree[b]+=1
                    succ[a].add(b)
                    break
        starts = []
        for key, val in in_degree.items():
            if val == 0:
                starts.append(key)
        # print(starts)
        output = ''
        while len(starts)>0:
            top = starts.pop(0)
            output+=top
            for nxt in succ[top]:
                in_degree[nxt]-=1
                if in_degree[nxt]==0:
                    starts.append(nxt)
        if set(output) != chars:
            return ""
        return output

