# time O(1)
# space: O(1)
from operator import mul, add, sub, truediv
class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        self.visited = [False for i in range(len(nums))]
        def backtrack(numbers):
            if len(numbers) == 0:
                return False
            if len(numbers)==1 and abs(numbers[0] - 24) < 1e-5:
                return True
            for a in range(len(numbers)):
                for b in range(len(numbers)):
                    if a!=b:
                        rest = [numbers[x] for x in range(len(numbers)) if a!=x and b!=x]
                        for op in [add, sub, mul, truediv]:
                            if op is truediv and numbers[b] == 0:
                                continue
                            c = op(numbers[a],numbers[b])
                            rest.append(c)
                            if backtrack(rest):
                                return True
                            rest.pop()
            return False
        return backtrack(nums)