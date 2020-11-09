# time O(N)
# space O(n)

class Solution:
    def solveEquation(self, equation: str) -> str:
        def helper(s):
            nums = 0
            x = 0
            sign =1
            i=0
            last_addition = 0
            while i < len(s):
                if s[i]=='+':
                    sign = 1
                elif s[i]=='-':
                    sign = -1
                elif s[i]=='x':
                    if i>0 and s[i-1].isdigit():
                        nums-=last_addition
                        x+=last_addition
                    else:
                        x+=sign
                else:
                    d = 0
                    while i<len(s) and s[i].isdigit():
                        d = d*10+int(s[i])
                        i+=1
                    last_addition=sign*d
                    nums+=last_addition
                    i-=1
                i+=1
            return nums, x
        
        left_nums, left_x = helper(left)
        right_nums, right_x = helper(right) 
        x=left_x-right_x
        nums=right_nums-left_nums
        if x == 0 and nums==0:
            return "Infinite solutions"
        if x == 0 and nums!=0:
            return "No solution"
        
        rem = nums//x
        if rem*x == nums:
            return f"x={rem}"
        return "No solution"
        