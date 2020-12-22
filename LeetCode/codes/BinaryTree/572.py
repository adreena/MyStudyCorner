# time O(MN)
# space O(M)
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def compare(s,t):
            if s is None and t is None:
                return True
            if s is None or t is None:
                return False
            return s.val==t.val and compare(s.left, t.left) and compare(s.right, t.right)
    
        
        if compare(s,t):
            return True
        if s:
            return self.isSubtree(s.left, t) or self.isSubtree(s.right,t)
        return False