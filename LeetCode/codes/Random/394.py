# time O(1)
# space O(N)
class Solution:
    def __init__(self, nums: List[int]):
        self.data=defaultdict(lambda:[])
        for i, num in enumerate(nums):
            self.data[num].append(i)

    def pick(self, target: int) -> int:
        if target in self.data:
            a = self.data[target].pop(0)
            self.data[target].append(a)
            return a