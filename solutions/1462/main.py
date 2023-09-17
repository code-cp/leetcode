from typing import * 
from collections import deque 
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adjcency_list = [[] for _ in range(numCourses)]
        for p in prerequisites: 
            adjcency_list[p[0]].append(p[1])
        
        def traverse(u, v):
            nonlocal adjcency_list
            nonlocal numCourses 
            visited = [0]*numCourses
            q = deque()
            
            q.append(u)
            visited[u] = 1 
            while len(q) > 0: 
                q_len = len(q) 
                for _ in range(q_len):
                    cur = q.popleft()
                    if cur == v:
                        return True 
                    for nxt in adjcency_list[cur]:
                        if visited[nxt] == 0:
                            visited[nxt] = 1
                            q.append(nxt)
        
            return False 
        
        ans = [False]*len(queries)
        for i, q in enumerate(queries): 
            if traverse(q[0], q[1]):
                ans[i] = True 
                
        return ans 