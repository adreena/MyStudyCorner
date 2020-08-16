# time: O(n)
# space: O(n)

class Solution:
    def numberToWords(self, num: int) -> str:
        words = {0:'', 1:'One', 2:'Two', 3:'Three', 4:'Four', 5:'Five', 6:'Six', 7:'Seven',\
                8:'Eight', 9:'Nine', 10:'Ten', 11:'Eleven', 12:'Twelve', 13:'Thirteen',\
                14:'Fourteen', 15:'Fifteen', 16:'Sixteen', 17:'Seventeen', 18:'Eighteen',\
                19:'Nineteen', 20:'Twenty', 30:'Thirty', 40:'Forty', 50:'Fifty', 60:'Sixty',\
                70:'Seventy', 80:'Eighty', 90:'Ninety', 100:'Hundred', 1000:'Thousand', \
                1000000:'Million', 1000000000:'Billion'}
        
        def translate(val, power):
            code = val*10**power 
            if code == 0:
                return []
            if power == 2:
                return [words[val], words[10**power ]]
            return [words[code]]
    
        output = []
        power = 0
        nxt_num = 0
        temp_output = []
        section = 0
        while num>0:
            temp = num%10
            if power == 1 and temp == 1:
                code = translate(temp*10+nxt_num, 0)
                temp_output = code 
            else:
                code = translate(temp, power)
                temp_output = code + temp_output
            nxt_num = temp
            num//=10
            power+=1
            if power >2 or num == 0:                
                if len(temp_output)>0:
                    if section >0:
                        output = temp_output + [words[10**section]] + output
                    else:
                        output = temp_output
                section+=3
                power = 0
                temp_output = []
        if len(output) == 0:
            return 'Zero'
        return ' '.join(output)
        