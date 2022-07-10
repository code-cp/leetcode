from typing import * 
import functools
class Solution:
    @staticmethod
    def checkValid(grid, pt):
        m, n = len(grid), len(grid[0])
        x, y = pt[0], pt[1]
        if x < 0 or x >= m:
            return False 
        if y < 0 or y >= n: 
            return False 
        if grid[x][y] == -1:
            return False 
        return True 
    def cherryPickup(self, grid: List[List[int]]) -> int:
        @functools.lru_cache(None)
        def dfs(p1, p2):
            # base case 
            # NOTE, need to return -float('inf') instead of 0 
            if not self.checkValid(grid, p1):
                return -float('inf')
            if not self.checkValid(grid, p2):
                return -float('inf') 
            # the number of cherries that can be picked up at current position 
            cherries = 0 
            x1, y1 = p1[0], p1[1]
            x2, y2 = p2[0], p2[1]
            m, n = len(grid), len(grid[0])
            cherries += grid[x1][y1]
            if not (x1 == x2 and y1 == y2):
                cherries += grid[x2][y2]
            if x1 == m-1 and x2 == m-1:
                return cherries
            cherries += max(
                dfs((x1+1, y1-1), (x2+1, y2-1)),
                dfs((x1+1, y1-1), (x2+1, y2)),
                dfs((x1+1, y1-1), (x2+1, y2+1)),
                dfs((x1+1, y1), (x2+1, y2-1)),
                dfs((x1+1, y1), (x2+1, y2)),
                dfs((x1+1, y1), (x2+1, y2+1)),
                dfs((x1+1, y1+1), (x2+1, y2-1)),
                dfs((x1+1, y1+1), (x2+1, y2)),
                dfs((x1+1, y1+1), (x2+1, y2+1)),
            )
            return cherries

        m, n = len(grid), len(grid[0])
        res = dfs((0,0), (0,n-1))
        return max(res, 0) 

if __name__ == "__main__": 
    s = Solution()

    grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
    assert s.cherryPickup(grid) == 24