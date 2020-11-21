# time O(N)
# space O(N)
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        tasks = [0 for i in range(n)]
        cur_time = 0
        stack = []
        for log in logs:
            i, tag, time = log.split(':')
            time = int(time)
            i = int(i)
            if tag == 'end':
                tasks[stack.pop()]+=time-cur_time+1
                cur_time = time+1
            elif tag== 'start':
                if stack:
                    tasks[stack[-1]]+=time-cur_time
                cur_time = time
                stack.append(i)
            
        return tasks
            