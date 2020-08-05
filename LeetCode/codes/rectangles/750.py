
# time: O(mn2)
# space: O(mn)

def countCornerRectangles(self, grid: List[List[int]]) -> int:
        active_cols = defaultdict(lambda:set())
        for i,row in enumerate(grid):
            for j , col in enumerate(row):
                if col == 1:
                    active_cols[i].add(j)
        
        total_rect = 0
        rows = sorted(list(active_cols.keys()))
        for i, row1 in enumerate(rows):
            for j in range(i+1, len(rows)):
                row2 = rows[j]
                temp = set.intersection(active_cols[row1], active_cols[row2])
                n = len(temp)
                if n >1:
                    total_rect += n*(n-1)//2
        return total_rect