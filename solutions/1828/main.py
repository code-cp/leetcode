from typing import * 

import math 
class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        dist = lambda x, y: math.sqrt((x[0]-y[0])**2+(x[1]-y[1])**2)

        n = len(queries)
        answer = [0]*n
        for i in range(n):
            q = queries[i] 
            for p in points: 
                if dist(q[:2], p) <= q[2]:
                    answer[i] += 1 
        return answer