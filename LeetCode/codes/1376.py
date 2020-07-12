# time: O(v+e)
# space O(v)

def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
    graph = defaultdict(lambda:[])
    for employee, manager in enumerate(manager):
        if manager != -1:
            graph[manager].append(employee)
    q = [(headID, informTime[headID])]
    max_time =informTime[headID] 
    visited = set()
    visited.add(headID)
    while len(q)>0:
        mng, time = q.pop(0)
        max_time = max(time, max_time)
        for e in graph[mng]:
            if e not in visited:
                visited.add(e)
                q.append((e, informTime[e]+time))
    return max_time