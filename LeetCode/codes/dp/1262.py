# time O(N)
# space O(1)
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        divs = [0, 0, 0]
        for x in nums:
            for y in divs[:]:
                idx = (y+x) % 3
                divs[idx] = max(divs[idx], y+x)
        return divs[0]