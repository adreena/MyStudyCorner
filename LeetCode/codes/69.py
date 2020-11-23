class Solution:
    def mySqrt(self, x: int) -> int:
        start = 0
        end = x
        while start<=end:
            mid = (start+end)//2
            num = mid*mid
            # print(num, mid)
            if num==x:
                return mid
            elif num<x:
                start=mid+1
            else:
                end=mid-1
        return end