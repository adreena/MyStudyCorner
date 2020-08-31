# time O(NM)
# space O(NM)

import copy
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        q = [(sr,sc)]
        oldColor = image[sr][sc]
        while len(q)>0:
            i, j = q.pop(0)
            image[i][j] = '*'
            for ni, nj in [(i+1,j), (i-1,j), (i, j+1), (i, j-1)]:
                if ni>=0 and ni<len(image) and nj>=0 and nj < len(image[0]) and \
                    image[ni][nj]== oldColor:
                    q.append((ni,nj))
                    
        for i in range(len(image)):
            for j in range(len(image[0])):
                if image[i][j]=='*':
                    image[i][j] = newColor
        return image