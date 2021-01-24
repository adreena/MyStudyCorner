# time : O(1)
# space: O(N)
class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.data=[]
        self.sum = 0
        self.cap = size
        self.size = 0
        

    def next(self, val: int) -> float:
        if self.size<self.cap:
            self.data.append(val)
            self.sum+=val
            self.size+=1
        else:
            f = self.data.pop(0)
            self.sum-=f
            self.sum+=val
            self.data.append(val)
        return self.sum/self.size

