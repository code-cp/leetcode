from typing import * 

class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        ans = 0 
        m, n = len(grid), len(grid[0]) 
        for i in range(m): 
            grid[i].sort(reverse=True) 
            
        for j in range(n): 
            vals = []
            for i in range(m): 
                vals.append(grid[i][j])
            ans += max(vals)
            
        return ans  