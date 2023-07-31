from typing import * 
from collections import deque 
class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        # NOTE, course index from 1 to n 
        adj_list = [[] for _ in range(n+1)]
        indegree = [0]*(n+1)
        for r in relations: 
            a, b = r[0], r[1]
            adj_list[a].append(b) 
            indegree[b] += 1 
          
        q = deque()
        # earliest times a course can finish 
        earliest_times = [0]*(n+1)
        for i in range(1, n+1): 
            if indegree[i] == 0: 
                q.append(i)
                # NOTE, time starts from index 0 
                earliest_times[i] = time[i-1]
        
        ans = 0   
        while len(q) > 0: 
            course = q.popleft()
            ans = max(ans, earliest_times[course])
            
            for nxt in adj_list[course]: 
                earliest_times[nxt] = max(earliest_times[nxt], earliest_times[course] + time[nxt-1])
                indegree[nxt] -= 1 
                if indegree[nxt] == 0: 
                    q.append(nxt)
                    
        return ans 
        
        