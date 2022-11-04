from typing import * 

import math 
class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        towers.sort()
        n = len(towers)

        calc_q = lambda q, d: math.floor(q / (1+d))
        dist = lambda p1, p2: math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
        def sum_q(x, y):
            res = 0
            p = (x, y)
            for t in towers: 
                d = dist((t[0], t[1]), p)
                if d > radius: 
                    continue 
                q = t[2]
                res += calc_q(q, d)
            return res 

        x_max = max(t[0] for t in towers)
        y_max = max(t[1] for t in towers)
        max_q = -1
        res = None  
        for x in range(x_max+1):
            for y in range(y_max+1): 
                q = sum_q(x, y)
                if q > max_q: 
                    max_q = q 
                    res = [x, y]

        return res 


if __name__ == "__main__": 
    s = Solution() 

    towers = [[42,0,0]]
    radius = 7
    assert s.bestCoordinate(towers, radius) == [0,0]

    towers = [[1,2,5],[2,1,7],[3,1,9]]
    radius = 2
    assert s.bestCoordinate(towers, radius) == [2,1]