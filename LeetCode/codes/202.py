#time:O(logN)
#space:O(1)
class Solution:
    def isHappy(self, n: int) -> bool:
        self.cache = set()
        def helper(num):
            if num ==0 or num==1:
                return True
            temp = 0
            while num>0:
                x = num%10
                temp+=x**2
                num//=10
            if temp == 1:
                return True
            if temp not in self.cache:
                self.cache.add(temp)
                return helper(temp)
            return False

        return helper(n)
