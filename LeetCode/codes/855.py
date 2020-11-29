# time O(logN)
# space O(N)
class ExamRoom:

    def __init__(self, N: int):
        self.cap = N
        self.seats = []

    def seat(self) -> int:
        if len(self.seats)==0:
            seat = 0
        else:
            dist, seat = self.seats[0], 0
            for i , s in enumerate(self.seats):
                if i>0:
                    prev = self.seats[i-1]
                    temp_dist = (s-prev)//2
                    if temp_dist>dist:
                        dist = temp_dist
                        seat = prev+dist
            d = self.cap - self.seats[-1] -1
            if d>dist:
                dist = d
                seat = self.cap-1
        print(self.seats)
        bisect.insort(self.seats,seat)
        return seat
    def leave(self, p: int) -> None:
        self.seats.remove(p)


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)