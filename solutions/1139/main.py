from typing import * 

class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0 

        # vertical prefix sum 
        v_memo = [[0]*n for _ in range(m)]
        for i in range(m): 
            for j in range(n): 
                if grid[i][j] == 0: 
                    continue 
                res = 1 
                v_memo[i][j] = v_memo[max(0, i-1)][j] + 1 
        
        # horizontal prefix sum 
        h_memo = [[0]*n for _ in range(m)]
        for i in range(m): 
            for j in range(n): 
                if grid[i][j] == 0: 
                    continue 
                res = 1
                h_memo[i][j] = h_memo[i][max(0, j-1)] + 1 

        for i in range(m): 
            for j in range(n): 
                # check bottom right 
                l_max = min(h_memo[i][j], v_memo[i][j])
                for k in range(l_max, 1, -1): 
                    # NOTE, i - k or i - k + 1? 
                    top = i - k + 1 
                    left = j - k + 1
                    if v_memo[i][left] < k: 
                        continue  
                    if h_memo[top][j] < k: 
                        continue 
                    res = max(k, res)
                    break 

        return res**2

if __name__ == "__main__": 
    s = Solution() 

    # [1,1,1]
    # [1,1,0]
    # [1,1,1]
    # [0,1,1]
    # [1,1,1]
    grid = [[1,1,1],[1,1,0],[1,1,1],[0,1,1],[1,1,1]]
    assert s.largest1BorderedSquare(grid) == 4   

    # # [0,1,1,1]
    # # [1,1,1,1]
    # # [1,0,0,1]
    # # [1,1,1,1]
    # # [1,0,1,1]
    # # [1,1,0,1]
    # grid = [[0,1,1,1],[1,1,1,1],[1,0,0,1],[1,1,1,1],[1,0,1,1],[1,1,0,1]]
    # assert s.largest1BorderedSquare(grid) == 4   

    # # [1,1,1,0]
    # # [1,0,1,1]
    # # [1,1,0,0]
    # # [1,1,1,1]
    # # [0,1,0,1]
    # grid = [[1,1,1,0],[1,0,1,1],[1,1,0,0],[1,1,1,1],[0,1,0,1]]
    # assert s.largest1BorderedSquare(grid) == 4   

    # grid = [[1,1,1],[1,0,1],[1,1,1]]
    # assert s.largest1BorderedSquare(grid) == 9    