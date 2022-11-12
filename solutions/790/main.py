class Solution:
    def numTilings(self, n: int) -> int:
        M = 10**9 + 7 
        dp = [[0 for _ in range(3)] for _ in range(n+1)]
        dp[0][0] = dp[1][0] = 1 

        for i in range(2, n+1):
            dp[i][0] = (dp[i-1][0] + dp[i-2][0] + dp[i-1][1] + dp[i-1][2]) % M 
            dp[i][1] = (dp[i-2][0] + dp[i-1][2]) % M  
            dp[i][2] = (dp[i-2][0] + dp[i-1][1]) % M 
        
        return (dp[-1][0]) % M 

if __name__ == "__main__": 
    s = Solution()

    assert s.numTilings(3) == 5 
