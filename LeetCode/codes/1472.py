# time O(1)
# space O(N)

class BrowserHistory:

    def __init__(self, homepage: str):
        self.hist = [homepage]
        self.cur, self.bound = 0, 0
        
    def visit(self, url: str) -> None:
        self.cur+=1
        if self.cur == len(self.hist):
            self.hist.append(url)
        else:
            self.hist[self.cur] = url
        self.bound = self.cur

    def back(self, steps: int) -> str:
        self.cur = max(0, self.cur-steps)
        return self.hist[self.cur]

    def forward(self, steps: int) -> str:
        self.cur = min(self.bound, self.cur+steps)
        return self.hist[self.cur]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)