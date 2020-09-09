
#time O(1) the roman numbers are finite
# space o(1) memory doesnt change based on the value of n

class Solution:
    def intToRoman(self, num: int) -> str:
        def helper(digit):
            romans = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M',
                        900:'CM', 400:'CD', 90:'XC', 40:'XL', 9: 'IX', 4: 'IV'}
            if digit in romans:
                temp = romans[digit]
            elif digit<5:
                temp  = romans[1]*digit
            elif digit<10:
                temp  = romans[5] + helper(digit-5)
            elif digit < 50:
                temp = romans[10]+helper(digit-10)
            elif digit < 100:
                temp = romans[50] + helper(digit-50)
            elif digit<500:
                temp = romans[100] + helper(digit-100)
            elif digit<1000:
                temp = romans[500] + helper(digit-500)
            else:
                temp = romans[1000] + helper(digit-1000)
            return temp
        
        convert = ''
        p=0
        while num>0:
            digit = num%10 * 10**p
            convert = helper(digit) + convert
            num //=10            
            p +=1
        return convert