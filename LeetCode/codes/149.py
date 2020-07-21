# time: O(n2)
# space: O(n)

from collections import defaultdict
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points)<=1:
            return len(points)
        points.sort(key=lambda x: x[0])
        equations = defaultdict(lambda:set())
        for i in range(len(points)-1):
            x1, y1 = points[i]
            for j in range(i+1,len(points)):
                x2, y2 = points[j]
                if x2==x1:
                    equations[(0, x2, 0)].add(i)
                    equations[(0, x2, 0)].add(j)
                else:
                    m = (y2-y1)/(x2-x1)
                    equations[(m,-m*x2,y2)].add(i)
                    equations[(m,-m*x2,y2)].add(j)
        if len(equations)==0:
            return 0
        lens = [len(val) for key, val in equations.items()]
        return max(lens)