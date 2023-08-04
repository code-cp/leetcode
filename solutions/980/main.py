from typing import * 

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        sx = -1 
        sy = -1 
        num = 1 
        m, n = len(grid), len(grid[0])
        
        def dfs(x, y, num):
            nonlocal grid
            nonlocal m 
            nonlocal n
            
            # base case 
            if x < 0 or x >= n or y < 0 or y >= m or grid[y][x] == -1: 
                return 0 
            if grid[y][x] == 2: 
                return 1 if num == 0 else 0 
            
            # recurse 
            grid[y][x] = -1 
            paths = dfs(x+1, y, num-1) + dfs(x-1, y, num-1) + dfs(x, y+1, num-1) + dfs(x, y-1, num-1) 
            grid[y][x] = 0
             
            return paths 
        
        for i in range(m):
            for j in range(n): 
                if grid[i][j] == 0: 
                    num += 1 
                elif grid[i][j] == 1: 
                    sx = j 
                    sy = i 
                    
        return dfs(sx, sy, num)

if __name__ == "__main__": 
    s = Solution()
    
    assert s.uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,2,-1]]) 