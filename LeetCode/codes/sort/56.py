
# time O(n)
# space: O(1)

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []
        intervals.sort(key=lambda x:x[0])
        
        output = [intervals.pop(0)]
        i = 1
        while intervals:
            temp = intervals.pop(0)
            if temp[0]<=output[-1][1]:
                output[-1][1] = max(output[-1][1], temp[1])
            else:
                output.append(temp)
        
        return output