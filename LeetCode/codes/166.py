class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        n = numerator
        d = denominator
        if n%d == 0:
            return str(n//d)
        
        output = ""

        if n/d<0:
            output +='-'
        n = abs(n)
        d = abs(d)
        output+=str(n//d)+'.'

        visited = {}
        decimal = ''

        i = 0
        n = n%d
        while n:
            if n in visited:
                prev = decimal[:visited[n]]
                rep = decimal[visited[n]:]
                if prev:
                    output+= prev+'('+rep+')'
                else:
                    output+= '('+rep+')'
                return output
            visited[n] = i
            n *=10
            decimal+=str(n//d)
            i+=1
            n %=d
        return output+decimal
