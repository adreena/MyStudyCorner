class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x:(x[0],-x[1]))
        lis = []
        for i in range(len(envelopes)):
            idx = bisect.bisect_left(lis, envelopes[i][1])
            if idx == len(lis):
                lis.append( envelopes[i][1])
            else:
                lis[idx] =  envelopes[i][1]
        # print(lis)
        return len(lis)