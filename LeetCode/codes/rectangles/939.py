# time: O(n2+nlogn)
# space: O(n)
from collections import defaultdict
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        X = defaultdict(lambda:[])
        for x,y in points:
            X[x].append(y)
        
        
        otherX = defaultdict()
        min_area = float('inf')
        for x in sorted(X):
            X[x].sort()
            for i in range(len(X[x])):
                y1 = X[x][i]
                for j in range(i):
                    y2 = X[x][j]
                    if (y1, y2) in otherX:
                        x2=otherX[(y1,y2)]
                        min_area = min(min_area, abs((y2-y1)*(x2-x)))
                    otherX[(y1,y2)] = x
        if min_area < float('inf'):
            return min_area
        return 0