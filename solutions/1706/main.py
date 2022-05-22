from typing import * 

class Solution:
    def dfs(self, grid, ball, row, col): 
        # base case 
        if row == len(grid): 
            self.answer[ball] = col 
            return 
        elif col == 0 and grid[row][col] == -1: 
            self.answer[ball] = -1 
            return
        elif col == len(grid[0])-1 and grid[row][col] == 1:
            self.answer[ball] = -1
            return
        elif col != len(grid[0])-1 and grid[row][col] == 1 and grid[row][col+1] == -1: 
            self.answer[ball] = -1
            return
        elif col != 0 and grid[row][col] == -1 and grid[row][col-1] == 1:
            self.answer[ball] = -1
            return

        self.dfs(grid, ball, row+1, col+grid[row][col])

    def findBall(self, grid: List[List[int]]) -> List[int]:
        self.answer = [0] * len(grid[0])
        for i in range(len(grid[0])): 
            self.dfs(grid, i, 0, i)
        return self.answer 

if __name__ == "__main__":
    s = Solution() 
    grid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]
    result = s.findBall(grid)
    assert result == [1,-1,-1,-1,-1]
    grid = [[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]
    result = s.findBall(grid)
    assert result == [0,1,2,3,4,-1]
    grid = [[1,-1,-1,1,-1,1,1,1,1,1,-1,1,1,1,1,1,1,-1,-1,-1,-1,-1,-1,1,-1,1,-1,1,-1,-1,-1,-1,1,-1,1,1,-1,-1,-1,-1,-1,1],[-1,1,1,1,-1,-1,-1,-1,1,1,1,-1,-1,-1,1,-1,-1,1,1,1,1,1,1,-1,1,-1,-1,-1,-1,-1,1,-1,1,-1,-1,-1,-1,1,1,-1,1,1],[1,-1,-1,-1,-1,1,-1,1,1,1,1,1,1,1,-1,1,-1,-1,-1,1,-1,-1,1,-1,1,-1,1,-1,-1,1,-1,1,-1,1,1,-1,-1,1,1,-1,1,-1]]
    result = s.findBall(grid)
    assert result == [-1,-1,1,-1,-1,-1,-1,10,11,-1,-1,12,13,-1,-1,-1,-1,-1,17,-1,-1,20,-1,-1,-1,-1,-1,-1,-1,-1,27,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]

