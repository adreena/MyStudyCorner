# time O()
# space O(1) # characters are constant
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        counter= Counter(tasks)
        available = []
        waiting = []
        time = 0
        for key, val in counter.items():
            available.append((-val,key))
        heapq.heapify(available)
        
        output = []
        finished=0
        while finished<len(tasks):
            while waiting and time-waiting[0][0]>n:
                tm, tk = waiting.pop(0)
                if counter[tk]>0:
                    heapq.heappush(available, (-counter[tk], tk))
            if available:
                tc, tk = heapq.heappop(available)
                output.append(tk)
                counter[tk]-=1
                if counter[tk]>0:
                    heapq.heappush(waiting, (time, tk))
                finished+=1
            else:
                output.append("idle")
            time+=1
        return len(output)
        
        
        
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        counter = [0 for i in range(26)]
        for t in tasks:
            counter[ord(t)-ord('A')]+=1
        
        counter.sort()
        fmax = counter.pop()
        wait = (fmax-1) * n
        while counter and wait>0:
            wait-=min(fmax-1, counter.pop())
        wait = max(0,wait)
        return wait+len(tasks)
        
        
        