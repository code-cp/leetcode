from typing import * 

class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        checkValid = lambda x, y: True if x[0] == y[0] or x[1] == y[1] else False 
        manhattanDist = lambda x, y: abs(x[0]-y[0]) + abs(x[1]-y[1])

        min_dist = float("inf")
        res = -1
        cur = [x, y]
        for i, p in enumerate(points): 
            if checkValid(cur, p):
                dist = manhattanDist(cur, p)
                if min_dist > dist:
                    min_dist = dist 
                    res = i 

        return res 

if __name__ == "__main__": 
    s = Solution() 

    x = 3
    y = 4
    points = [[1,2],[3,1],[2,4],[2,3],[4,4]]
    assert s.nearestValidPoint(x, y, points) == 2 