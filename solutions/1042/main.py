from typing import * 

class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        ans = [0]*n 
        # NOTE, adj cannot use {}, since paths may be [] when n = 1 
        adj = [[] for _ in range(n)]
        for p in paths: 
            adj[p[0]-1].append(p[1]-1)
            adj[p[1]-1].append(p[0]-1)
        for i in range(n): 
            # colored[0] means uncolored 
            colored = [False]*5 
            for v in adj[i]: 
                colored[ans[v]] = True 
            for j in range(1, 5): 
                if colored[j] == False: 
                    ans[i] = j 
                    break 
        return ans 

if __name__ == "__main__": 
    s = Solution()
   
    n = 1
    paths = []
    assert s.gardenNoAdj(n, paths) == [1]
    
    n = 3
    paths = [[1,2],[2,3],[3,1]]
    assert s.gardenNoAdj(n, paths)