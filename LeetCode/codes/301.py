# time O(2^N)
# space O(N)
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        self.min_removed = float('inf')
        self.outputs = set()
        def backtrack(num_left, num_right, s_idx, removed, output):
            if s_idx == len(s) and num_left==num_right:
                if removed<self.min_removed:
                    self.outputs=set()
                    self.min_removed=removed
                if self.min_removed==removed:
                    self.outputs.add(output)
            elif s_idx<len(s):
                if s[s_idx]!='(' and s[s_idx]!=')':
                    backtrack(num_left, num_right, s_idx+1, removed, output+s[s_idx])
                else:
                    # remove
                    backtrack(num_left, num_right, s_idx+1, removed+1, output)
                    if s[s_idx]=='(':
                        backtrack(num_left+1, num_right, s_idx+1, removed, output+'(')
                    elif num_left>num_right:
                        backtrack(num_left, num_right+1, s_idx+1, removed, output+')')
        backtrack(0,0,0,0,'')
        return self.outputs