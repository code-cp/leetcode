from typing import * 

class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        grid = [[1 for _ in range(n)] for _ in range(n)]
        for m in mines: 
            grid[m[0]][m[1]] = 0 

        left = [[0 for _ in range(n)] for _ in range(n)]
        right = [[0 for _ in range(n)] for _ in range(n)] 
        up = [[0 for _ in range(n)] for _ in range(n)]
        down = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n): 
            for j in range(n): 
                if j > 0 and grid[i][j] == 1: 
                    left[i][j] = left[i][j-1] + 1 
                else: 
                    left[i][j] = grid[i][j]

        for i in range(n): 
            for j in range(n-1,-1,-1):
                if j < n-1 and grid[i][j] == 1:
                    right[i][j] = right[i][j+1] + 1
                else: 
                    right[i][j] = grid[i][j]

        for i in range(n): 
            for j in range(n):
                if i > 0 and grid[i][j] == 1:
                    up[i][j] = up[i-1][j] + 1
                else: 
                    up[i][j] = grid[i][j]

        for i in range(n-1,-1,-1): 
            for j in range(n):
                if i < n-1 and grid[i][j] == 1:
                    down[i][j] = down[i+1][j] + 1
                else: 
                    down[i][j] = grid[i][j]

        res = 0 
        for i in range(n): 
            for j in range(n):
                min_val = min(left[i][j], right[i][j], up[i][j], down[i][j])
                res = max(min_val, res)

        return res  

    
if __name__ == "__main__": 
    s = Solution() 

    n = 5
    mines = [[4,2]]
    assert s.orderOfLargestPlusSign(n, mines) == 2 