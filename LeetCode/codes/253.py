# time: O(NlogN)
# space: O(N)

def minMeetingRooms(self, intervals: List[List[int]]) -> int:
    if len(intervals)==0:
        return 0
    intervals.sort(key=lambda x: x[0])
    rooms = [intervals[0][1]]
    for start, end in intervals[1:]:
        if len(rooms)>0 and start >= rooms[0]:
            heapq.heappop(rooms)
        heapq.heappush(rooms, end)
    return len(rooms)
