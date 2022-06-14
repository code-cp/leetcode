from typing import * 

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        res = []
        m, n = len(mat), len(mat[0])
        def inMat(i, j): 
            return 0 <= i < m and 0 <= j < n 
        i, j = 0, 0 
        dx, dy = -1, 1 
        while i < m and j < n:  
            res.append(mat[i][j])
            i_ne, j_ne = i+dx, j+dy
            if not inMat(i_ne, j_ne): 
                if i_ne < 0 or i_ne > m-1:
                    if j_ne < n: 
                        i_ne, j_ne = i, j+abs(dy)
                    else: 
                        i_ne, j_ne = i+abs(dy), j
                elif j_ne < 0 or j_ne > n-1: 
                    if i_ne < m:
                        i_ne, j_ne = i+abs(dx), j
                    else: 
                        i_ne, j_ne = i, j+abs(dx)
                dx *= -1
                dy *= -1  
            i, j = i_ne, j_ne 
        return res 
            

if __name__ == "__main__": 
    s = Solution()

    mat = [[1,2,3],[4,5,6],[7,8,9]]
    assert s.findDiagonalOrder(mat) == [1,2,4,7,5,3,6,8,9]
