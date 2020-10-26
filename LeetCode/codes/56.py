# time O(NlogN)
# space: O(N)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []
        intervals.sort()
        output = [intervals[0]]
        for s,e in intervals[1:]:
            if s<=output[-1][1]:
                output[-1][1] = max(e, output[-1][1])
            else:
                output.append([s,e])
        return output