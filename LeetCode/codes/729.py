class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right= None
    
    def insert(self, start, end):
        if end <=self.start:
            if self.left is None:
                self.left = Node(start, end)
                return True
            return self.left.insert(start,end)
        elif start>=self.end:
            if self.right is None:
                self.right = Node(start,end)
                return True
            return self.right.insert(start,end)
        return False
                
class MyCalendar:

    def __init__(self):
        self.cal= None
        
    def book(self, start: int, end: int) -> bool:
        if not self.cal:
            self.cal = Node(start,end)
            return True
        else:
            return self.cal.insert(start,end)

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)