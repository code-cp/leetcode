from typing import * 
from collections import deque 
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        management = {}
        for i, m in enumerate(manager): 
            management[m] = management.get(m,[])
            management[m].append(i)
        
        q = deque()
        q.append((headID,0))
        ans = 0 
        while len(q) > 0: 
            q_len = len(q)
            for _ in range(q_len): 
                idx, t = q.popleft()
                new_t = t+informTime[idx]
                ans = max(ans,new_t)
                if idx not in management: 
                    continue 
                for i in management[idx]: 
                    q.append((i,new_t))
        
        return ans 
    
if __name__ == "__main__": 
    s = Solution() 

    assert s.numOfMinutes(6, 2, [2,2,-1,2,2,2], [0,0,1,0,0,0]) == 1 
    assert s.numOfMinutes(1, 0, [-1], [0]) == 0 
        