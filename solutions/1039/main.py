from typing import * 

# ref https://leetcode.cn/problems/minimum-score-triangulation-of-polygon/solutions/2203005/shi-pin-jiao-ni-yi-bu-bu-si-kao-dong-tai-aty6/

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        dp = [[float("inf")]*n for _ in range(n)]
        # init: all polygons that only have two points are invalid 
        for i in range(n-1): 
            dp[i][i+1] = 0
        # NOTE, k > i, so i reverse iterate 
        for i in range(n-3,-1,-1):
            # NOTE, k < j, so j do not need reverse 
            for j in range(i+2,n):
                temp = []
                for k in range(i+1,j):
                    dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j]+values[i]*values[k]*values[j])
        return dp[0][-1]
                
if __name__ == "__main__": 
    s = Solution() 
    
    assert s.minScoreTriangulation([1,3,1,4,1,5]) == 13 