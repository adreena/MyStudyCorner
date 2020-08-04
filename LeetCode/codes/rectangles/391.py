# time : O(n)
# space: O(1)

class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        if len(rectangles) == 0:
            return True
        min_x, min_y, max_x, max_y = rectangles[0]
        total_area = 0
        corners = set()
        for x1,y1, x2,y2 in rectangles:
            total_area+= (y2-y1)*(x2-x1)
            min_x = min(x1,min_x)
            max_x = max(x2,max_x)
            min_y = min(y1, min_y)
            max_y = max(y2, max_y)
            corners^={(x1,y1), (x1,y2), (x2,y1), (x2,y2)}
        if {(min_x, min_y), (min_x, max_y), (max_x, min_y), (max_x,max_y)} != corners:
            return False
        return total_area == (max_y-min_y)*(max_x - min_x)