# time catalan numbers (2n n)*1/n
# space: catalan numbers

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.outputs = []
        def helper(n_left, n_right, output):
            if n_left == 0 and n_right == 0:
                self.outputs.append(output)
            else:
                if n_left>0:
                    helper(n_left-1, n_right, output+'(')
                if n_right>n_left:
                    helper(n_left, n_right-1, output+')')
        helper(n,n,'')
        return self.outputs