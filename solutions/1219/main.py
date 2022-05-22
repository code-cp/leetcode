from typing import List 

class Solution:
    def __init__(self): 
        self.max_gold = 0
    def backtracking(self, grid, i, j, visited, result):
        m, n = len(grid), len(grid[0])
        dirs = [[0,1], [1,0], [0,-1], [-1,0]]
        for d in dirs: 
            x_new, y_new = i + d[0], j + d[1]
            if x_new < 0 or x_new >= m or y_new < 0 or y_new >= n: 
                continue 
            if grid[x_new][y_new] == 0:
                continue 
            if visited[x_new][y_new] == 1: 
                continue 
            visited[x_new][y_new] = 1 
            self.backtracking(grid, x_new, y_new, visited, result + grid[x_new][y_new])
            visited[x_new][y_new] = 0
        # dead end (base case) 
        self.max_gold = max(result, self.max_gold)
        return result
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for i in range(m): 
            for j in range(n): 
                if grid[i][j] == 0: 
                    continue 
                visited = [[0] * n for _ in range(m)]
                visited[i][j] = 1 
                self.backtracking(grid, i, j, visited, grid[i][j])
        return self.max_gold

if __name__ == "__main__": 
    grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
    s = Solution()
    assert s.getMaximumGold(grid) == 28