from typing import * 

class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        line = lambda t, x, m: t[1] - x[1] - m * (t[0] - x[0]) 

        p1 = [float(x) for x in points[0]]
        p2 = [float(x) for x in points[1]]
        p3 = [float(x) for x in points[2]]

        if p1[0] == p2[0] == p3[0]: 
            return False 
        if p1[1] == p2[1] == p3[1]:
            return False  

        if p1[0] - p2[0] == 0: 
            return p1[1] - p2[1] != 0  
        slope = (p1[1] - p2[1]) / (p1[0] - p2[0]) 

        return abs(line(p3, p1, slope)) > 1e-4 


if __name__ == "__main__": 
    s = Solution() 

    points = [[1,1],[2,3],[3,2]]
    assert s.isBoomerang(points)

    points = [[0,0],[0,2],[2,1]]
    assert s.isBoomerang(points)

    points = [[1,1],[2,2],[3,3]]
    assert not s.isBoomerang(points) 

    points = [[0,1],[0,1],[2,1]]
    assert not s.isBoomerang(points) 

    points = [[0,2],[0,1],[0,1]]
    assert not s.isBoomerang(points) 

    points = [[0,2],[0,2],[2,0]]
    assert not s.isBoomerang(points)

    points = [[49,56],[71,71],[5,26]]
    assert not s.isBoomerang(points)

    points = [[0,1],[2,0],[1,1]]
    assert s.isBoomerang(points)