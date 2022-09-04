from typing import * 

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        rows = [0] * m 
        cols = [0] * n 
        cnt = 0 
        for i in range(m): 
            for j in range(n): 
                if mat[i][j] == 1:
                    rows[i] += 1 
                    cols[j] += 1 
        for i in range(m): 
            for j in range(n): 
                if mat[i][j] == 1:
                    if rows[i] == 1 and cols[j] == 1:
                        cnt += 1 
        return cnt 

if __name__ == "__main__": 
    s = Solution()

    mat = [[1,0,0],[0,1,0],[0,0,1]]
    assert s.numSpecial(mat) == 3 