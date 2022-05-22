from typing import List 

class Solution:
    def shouldVisit(self, grid, row, col, oldColor, visited):
        if row < 0 or col < 0 or row > len(grid)-1 or col > len(grid[0])-1:
            # check if inside grid
            return False
        elif visited[row][col] != 0:
            # check if visited
            return False
        elif grid[row][col] != oldColor:
            return False
        else:
            return True

    def dfs(self, grid, row, col, oldColor, visited):
        # base case
        if not self.shouldVisit(grid, row, col, oldColor, visited):
            return
        else:
            visited[row][col] = 1

        # do color
        # up, down, left, right
        dirRow = [-1, 1, 0, 0]
        dirCol = [0, 0, -1, 1]

        if row == 0 or col == 0 or row == len(grid)-1 or col == len(grid[0])-1:
            # check if on border
            visited[row][col] = 2
        else:
            # check if adjacent to different color
            for i in range(len(dirRow)):
                if grid[row+dirRow[i]][col+dirCol[i]] != oldColor:
                    visited[row][col] = 2
                    break

        # dfs
        for i in range(len(dirRow)):
            self.dfs(grid, row+dirRow[i], col+dirCol[i], oldColor, visited)

    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        visited = [[0] * len(grid[0]) for _ in range(len(grid))]
        oldColor = grid[row][col]
        self.dfs(grid, row, col, oldColor, visited)
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if visited[row][col] == 2:
                    grid[row][col] = color
        return grid

if __name__ == "__main__":
    grid = [[1,1,1],[1,1,1],[1,1,1]]
    row, col = 1, 1
    color = 2
    ans = [[2,2,2],[2,1,2],[2,2,2]]
    s = Solution()
    grid = s.colorBorder(grid, row, col, color)
    for row in range(len(grid)): 
        assert grid[row] == ans[row]
