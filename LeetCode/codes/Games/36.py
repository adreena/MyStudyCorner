#time O(MN)
# space O(1)

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        visited = set()
        for i in range(0,9):
            for j in range(0,9):
                if board[i][j] != '.':
                    current = board[i][j]
                    
                    if (i, current) in visited or (current,j) in visited or (i//3,j//3,current) in visited:
                        return False
                    visited.add((i,current))
                    visited.add((current,j))
                    visited.add((i//3,j//3,current))
        return True


        # n = 9        
        # boxes= defaultdict(lambda:set())
        # cols = {i:set() for i in range(n)}
        # rows = {i:set() for i in range(n)}
        
        # def find_idx(x):
        #     ranges = [[0,3],[3,6],[6,9]]
        #     for r_id, r in enumerate(ranges):
        #         if r[0]<=x<r[1]:
        #             return r_id
                
        # for i in range(n):
        #     for j in range(n):
        #         if board[i][j]!='.':
        #             col_box = find_idx(j)
        #             row_box = find_idx(i)
        #             if not(1<=int(board[i][j])<=9) or board[i][j] in cols[j] or board[i][j] in rows[i] or board[i][j]  in boxes[(row_box,col_box)]:
        #                 return False
        #             cols[j].add(board[i][j])
        #             rows[i].add(board[i][j])
        #             boxes[(row_box,col_box)].add(board[i][j])
        # return True