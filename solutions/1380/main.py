from typing import List 

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        row_min, col_max = [], []
        m, n = len(matrix), len(matrix[0])
        # for row 
        for i in range(m): 
            rmin = float("inf")
            for j in range(n):
                if matrix[i][j] < rmin: 
                    rmin = matrix[i][j] 
            row_min.append(rmin)
        # for col 
        for j in range(n): 
            cmax = -float("inf")
            for i in range(m):
                if matrix[i][j] > cmax: 
                    cmax = matrix[i][j] 
            col_max.append(cmax)
        # traverse matrix 
        result = []
        for i in range(m): 
            for j in range(n):
                if matrix[i][j] in row_min and matrix[i][j] in col_max:
                    result.append(matrix[i][j])
        return result

if __name__ == "__main__": 
    matrix = [[7,8],[1,2]]
    s = Solution()
    assert s.luckyNumbers(matrix) == [7]