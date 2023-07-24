from typing import * 
import heapq 
from collections import deque 
class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        # val = yi + yj + |xi - xj| = yi + yj + xj - xi 
        # val = xj + yj + yi - xi 
        def calVal(idx): 
            nonlocal points 
            return points[idx][1] - points[idx][0]
        
        q = deque()
        res = -float("inf") 
        for j, p in enumerate(points): 
            # pop the indices that are too old 
            while len(q) > 0 and points[j][0] - points[q[0]][0] > k: 
                q.popleft()
            
            if len(q) > 0: 
                # fix j, find max val 
                cur = calVal(q[0]) + points[j][0] + points[j][1]
                res = max(res, cur)
            
            # if new val at index j is better, then we will never use the vals before index j 
            while len(q) > 0 and calVal(q[-1]) < calVal(j): 
                q.pop()
                
            q.append(j)
                
        return res 
    
if __name__ == "__main__": 
    s = Solution()
    
    assert s.findMaxValueOfEquation([[0,0],[3,0],[9,2]], 3) == 3 