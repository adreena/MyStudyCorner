
# time O(1) for 300 seconds
# space O(1)

class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hits = {i:[0,0] for i in range(300)}

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        idx = timestamp%300
        if self.hits[idx][0]==timestamp:
            self.hits[idx][1]+=1
        else:
            self.hits[idx][0] = timestamp
            self.hits[idx][1] = 1

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        total = 0
        for key, val in self.hits.items():
            if timestamp-val[0]<300:
                total+=val[1]
        return total



# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
