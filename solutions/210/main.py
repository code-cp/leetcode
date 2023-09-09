from typing import * 
from collections import deque 
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjacency_list = [[] for _ in range(numCourses)]
        for p in prerequisites: 
            adjacency_list[p[1]].append(p[0])
        
        stack = deque()
        has_cycle = False 
        visited = [0]*numCourses
        on_path = [0]*numCourses 
        def traverse(cur): 
            nonlocal adjacency_list 
            nonlocal visited 
            nonlocal on_path 
            nonlocal has_cycle 
            
            if has_cycle: 
                return 
            
            if on_path[cur] == 1: 
                has_cycle = True 
                return 
            
            if visited[cur] == 1:
                return 
            visited[cur] = 1 
            
            on_path[cur] = 1 
            for v in adjacency_list[cur]: 
                traverse(v)
            stack.append(cur) 
            on_path[cur] = 0 
            
        for cur in range(numCourses): 
            traverse(cur)
            
        if has_cycle:
            return []
        else: 
            return list(reversed(stack)) 