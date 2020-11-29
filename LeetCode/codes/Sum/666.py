class Solution:
    def pathSum(self, nums: List[int]) -> int:
        
        tree = defaultdict(lambda:0)
        for i, num in enumerate(nums):
            depth, pos, v = num//100 , (num//10) %10, num%10
            if i == 0:
                tree[(depth,pos)]=v
            else:
                tree[(depth,pos)]+=tree[(depth-1, (pos+1)//2)] +v
        # print(tree)
        sums = 0
        for depth, pos in tree.keys():
            if (depth+1,pos*2 -1) in tree or (depth+1, pos*2)  in tree: # not leaf
                continue
            sums+=tree[(depth,pos)]
        return sums