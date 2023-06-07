from typing import * 

inf = float("inf")

class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        # dp[i][j] means tree is arr[i:j]
        # dp is smallest sum of all non leaf nodes 
        # dp[i][j] = min(dp[i][k] + dp[k+1][j] + m_ik * m_(k+1)j)
        # m_ik means the max. in arr[i,k]
        
        n = len(arr)
        dp = [[inf]*n for _ in range(n)]
        mval = [[0]*n for _ in range(n)]
        for j in range(n): 
            mval[j][j] = arr[j]
            dp[j][j] = 0 
            for i in range(j-1, -1, -1): 
                # mval[i+1][j] means the max for [i+1,j]
                # max([i,j]) = max(arr[i], max([i+1,j]))
                mval[i][j] = max(arr[i], mval[i+1][j])
                for k in range(i,j): 
                    dp[i][j] = min(dp[i][j], dp[i][k]+dp[k+1][j]+mval[i][k]*mval[k+1][j]) 
        
        return dp[0][n-1]
    
if __name__ == "__main__": 
    s = Solution() 
    
    assert s.mctFromLeafValues([6,2,4]) == 32 