from typing import * 

class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        col = []
        m, n = len(score), len(score[0])
        for i in range(m): 
            col.append(score[i][k])
        idxs = sorted(range(len(col)), key=lambda j: col[j], reverse=True)
        res = [[0]*n for _ in range(m)]
        for i in range(m): 
            for j in range(n): 
                res[i][j] = score[idxs[i]][j]
        return res 
