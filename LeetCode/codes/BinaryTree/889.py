# time O(Nk)
# space O(logn)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        
        def helper(pre_i, post_i, N):
            if N==0:
                return None
            if N == 1:
                return TreeNode(pre[pre_i])
            k = 0
            while k<N:
                if post[post_i+k-1]!=pre[pre_i+1]:
                    k+=1
                else:
                    break
            node = TreeNode(pre[pre_i])
            node.left = helper(pre_i+1, post_i,k)
            node.right = helper(pre_i+1+k, post_i+k,N-k-1)
            return node
        
        return helper(0,0,len(pre))

class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        
        if len(pre)==0:
            return None
        stack = [TreeNode(pre[0])]
        j = 0
        for i in range(1, len(pre)):
            node = TreeNode(pre[i])
            while stack[-1].val==post[j]:
                stack.pop()
                j+=1
            
            if stack[-1].left is None:
                stack[-1].left = node
            else:
                stack[-1].right = node
            stack.append(node)
        
        return stack[0]