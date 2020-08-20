# time: O(3^N)
# space O(3^N)
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numbers = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', \
                   '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        
        def helper(digits):
            if len(digits)==0:
                return []
            elif len(digits)==1:
                return list(numbers[digits[0]])
            
            first= helper(digits[0])
            rest = helper(digits[1:])
            output = []
            for f in first:
                for r in rest:
                    output.append(f'{f}{r}')
            return output
        return helper(digits)
