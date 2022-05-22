from typing import * 

class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        bot_area = n ** 2 - len([(ix, iy) for ix, row in enumerate(grid) for iy, i in enumerate(row) if i == 0])
        y_area = sum([max(row) for row in grid])
        z_area = sum([max([row[i] for row in grid]) for i in range(n)])
        return bot_area + y_area + z_area 

if __name__ == "__main__": 
    s = Solution()

    # grid = [[1,2],[3,4]]
    # assert s.projectionArea(grid) == 17 

    grid = [[1,0],[0,2]]
    assert s.projectionArea(grid) == 8 
