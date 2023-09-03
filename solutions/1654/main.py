from typing import * 
from collections import deque 
class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        # if cur <= limit, can go right 
        # if last time = right, then can go left
        steps = 0
        if x == 0: 
            return steps 
        
        max_f = max(forbidden)
        limit = max(x, max_f) + b 
        
        visited = [[0]*2 for _ in range(8001)] 
        for f in forbidden: 
            visited[f][0] = -1
            visited[f][1] = -1 
            
        q = deque()
        q.append((0, 0))
        
        while len(q) > 0: 
            l = len(q) 
            steps += 1 
            for _ in range(l):
                # i is current position 
                # k is the state 
                i, k = q.popleft()
                
                if i <= limit and visited[i+a][0] == 0:
                    # go right  
                    visited[i+a][0] = 1
                    q.append((i+a, 0))
                    if i+a == x: 
                        return steps 
                 
                # previous is move right, so we can move left now    
                if k == 0: 
                    if i-b >= 0 and visited[i-b][1] == 0:
                        visited[i-b][1] = 1
                        q.append((i-b, 1))
                        if i-b == x:
                            return steps 
                        
        return -1 