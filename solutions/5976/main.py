from typing import List 

class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        for i in range(n):
            recordRow = [0]*n
            recordCol = [0]*n
            for j in range(n):
                recordRow[matrix[i][j]-1] = 1
                recordCol[matrix[j][i]-1] = 1
            if sum(recordRow) != n or sum(recordCol) != n:
                return False
        return True

if __name__ == "__main__": 
    matrix = [[1,2,3],[3,1,2],[2,3,1]]
    s = Solution()
    assert s.checkValid(matrix)
