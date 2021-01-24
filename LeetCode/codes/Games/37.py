class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        cols = {i:set() for i in range(n)}
        rows=  {i:set() for i in range(n)}
        boxes=defaultdict(lambda:set())
        ranges=[(0,3),(3,6),(6,9)]
        
        def get_ranges(ci,cj):
            boxi,boxj=0,0
            for cid, r in enumerate(ranges):
                if r[0]<=ci<r[1]:
                    boxi=cid
                    break
            for cid, r in enumerate(ranges):
                if r[0]<=cj<r[1]:
                    boxj=cid
                    break
            return boxi,boxj
        
        def check(ci,cj,cv):
            for i in range(n):
                if board[ci][i]==cv:
                    return False
            for i in range(n):
                if board[i][cj]==cv:
                    return False
            ri, rj = get_ranges(ci,cj)
            for i in range(*ranges[ri]):
                for j in range(*ranges[rj]):
                    if board[i][j]==cv:
                        return False
            return True
        
        
        def empty():
            for i in range(n):
                for j in range(n):
                    if board[i][j]==".":
                        return (i,j)
            return False
        def backtrack():
            e = empty()
            if not e:
                return True
            if e:
                i, j = e
                for v in range(1,10):
                    if check(i,j, str(v)):
                        board[i][j]=str(v)
                        if backtrack():
                            return True
                        board[i][j]='.'
                        
            return False
        backtrack()
        return board