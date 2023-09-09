from typing import * 

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = [0]*numCourses
        adjacency_list = [[] for _ in range(numCourses)]
        for p in prerequisites: 
            adjacency_list[p[1]].append(p[0])
        
        # topological sort 
        has_cycle = False 
        on_path = [0]*numCourses 
        def traverse(cur): 
            nonlocal adjacency_list 
            nonlocal visited 
            nonlocal has_cycle
            nonlocal on_path
            
            if has_cycle:
                return 
                        
            if on_path[cur] == 1: 
                # this means on_path is already marked for cur vertex  
                has_cycle = True 
                return 
            
            # note, need to check on_path first 
            if visited[cur] == 1: 
                return 
            visited[cur] = 1 

            # mark the vertex to be on path
            # NOTE, need to mark it here right before for loop 
            on_path[cur] = 1            
            for v in adjacency_list[cur]:
                traverse(v)
            # mark cur vertex as false when finished 
            on_path[cur] = 0  
            
        for i in range(numCourses):
            traverse(i)
            
        return not has_cycle 

        
if __name__ == '__main__': 
    s = Solution()
    
    # assert s.canFinish(2, [[1,0],[0,1]]) == False 
    assert s.canFinish(5, [[1,4],[2,4],[3,1],[3,2]]) == True  