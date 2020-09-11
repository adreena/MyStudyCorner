class Solution:
    def numberToWords(self, num: int) -> str:
        words = {0:'', 1:'One', 2:'Two', 3:'Three', 4:'Four', 5:'Five', 6:'Six', 7:'Seven',\
                8:'Eight', 9:'Nine', 10:'Ten', 11:'Eleven', 12:'Twelve', 13:'Thirteen',\
                14:'Fourteen', 15:'Fifteen', 16:'Sixteen', 17:'Seventeen', 18:'Eighteen',\
                19:'Nineteen', 20:'Twenty', 30:'Thirty', 40:'Forty', 50:'Fifty', 60:'Sixty',\
                70:'Seventy', 80:'Eighty', 90:'Ninety', 100:'Hundred', 1000:'Thousand', \
                1000000:'Million', 1000000000:'Billion'}


        if num == 0:
            return 'Zero'
        unit = 0
        output = ''
        while num>0:
            prev_digit = 0
            temp = []
            for i in range(3):
                digit = num%10
                if i == 2:
                    to_add  = words[digit]+' '+ words[10**i]
                    if digit == 0:
                        to_add = ''
                elif i == 1:
                    if digit == 1:
                        to_add = words[10+prev_digit]
                        if temp:
                            temp.pop()
                    else:
                        to_add = words[digit*10**i]
                else:
                    to_add = words[digit]
                if to_add!='':
                    temp.append(to_add)
                num //=10
                prev_digit = digit
                if num == 0:
                    break
            temp =  ' '.join(temp[::-1])
            if temp!='':
                if unit>0 and temp!='':
                    if output == '':
                        output = temp + ' '+ words[1000**unit]
                    else:
                        output = temp + ' ' + words[1000**unit] + ' ' + output
                else:
                    output = temp
            unit+=1
        return output
