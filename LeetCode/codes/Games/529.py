    # time O(MN)
    # space: O(1)
    
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if len(board)==0:
            return board
        n, m = len(board), len(board[0])
        q = [click]
        visited = set()
        while q:
            ci, cj = q.pop(0)
            visited.add((ci,cj))
            if board[ci][cj] == 'M':
                board[ci][cj] = 'X'
                break
            if board[ci][cj] == 'E':
                count = 0
                temp = []
                for ni, nj in [(ci+1, cj), (ci+1,cj+1), (ci+1,cj-1),
                               (ci, cj+1), (ci, cj-1),
                               (ci-1, cj), (ci-1, cj+1), (ci-1, cj-1)]:
                    if 0<=ni<n and 0<=nj<m:
                        if board[ni][nj]=='M':
                            count+=1
                        elif board[ni][nj]=='E' and (ni,nj) not in visited:
                            temp.append((ni,nj))
                if count >0:
                    board[ci][cj] = str(count)
                else:
                    board[ci][cj] = 'B'
                    if temp:
                        q.extend(temp)     
        return board