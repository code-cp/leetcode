from typing import * 

class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        row_add = [0] * m 
        col_add = [0] * n 
        for d in indices: 
            row_add[d[0]] += 1 
            col_add[d[1]] += 1
        # NOTE the pattern (() for for) 
        return sum((row + col) % 2 for row in row_add for col in col_add)