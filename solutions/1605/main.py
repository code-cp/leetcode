from typing import * 
import math 
class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m, n = len(rowSum), len(colSum)
        res = [[0]*n for _ in range(m)]
        total = sum(rowSum) + sum(colSum)
        cur = 0 
        while True: 
            minr = min(rowSum)
            minri = min(range(m), key=rowSum.__getitem__)
            minc = min(colSum)
            minci = min(range(n), key=colSum.__getitem__)
            
            min_val = min(minr, minc)
            if math.isfinite(min_val):
                res[minri][minci] += min_val
                cur += min_val
            else: 
                break 
            
            rowSum[minri] = max(0, rowSum[minri] - min_val) 
            if rowSum[minri] == 0: 
                rowSum[minri] = float("inf")
            colSum[minci] = max(0, colSum[minci] - min_val) 
            if colSum[minci] == 0: 
                colSum[minci] = float("inf")
                
        return res 
    
if __name__ == "__main__": 
    s = Solution() 
    
    rowSum = [3,8]
    colSum = [4,7]
    assert s.restoreMatrix(rowSum, colSum)
            