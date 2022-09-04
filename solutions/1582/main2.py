from typing import * 

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        sr = [sum(r) for r in mat]
        sc = [sum(c) for c in zip(*mat)]
        return sum(mat[i][j] == 1 and sr[i] == 1 and sc[j] == 1 for i in range(len(mat)) for j in range(len(mat[0])))

if __name__ == "__main__": 
    s = Solution()

    mat = [[1,0,0],[0,1,0],[0,0,1]]
    assert s.numSpecial(mat) == 3 