from typing import List 

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        rowMax = [0]*len(grid)
        colMax = [0]*len(grid[0])

        for i in range(len(grid)):
            rowMax[i] = max(grid[i])
        for i in range(len(grid[0])):
            colMax[i] = max([grid[j][i] for j in range(len(grid))])

        total = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                total += min(rowMax[i], colMax[j]) - grid[i][j]
                grid[i][j] = min(rowMax[i], colMax[j])

        return total

if __name__ == "__main__": 
    grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
    s = Solution()
    ans = 35
    assert s.maxIncreaseKeepingSkyline(grid) == ans 

