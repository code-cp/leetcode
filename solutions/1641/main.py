class Solution:
    def countVowelStrings(self, n: int) -> int:
        chars = ["a","e","i","o","u"]
        m = len(chars)
        # dp[i][j] means num for len i, end with char j 
        # dp[i][j] = sum(dp[i-1][k]), j >= k 
        dp = [[0]*m for _ in range(n+1)]
        # init 
        for i in range(m):
            dp[1][i] = 1 
        for i in range(1, n+1):
            dp[i][0] = 1 
        # iterate 
        for i in range(2, n+1): 
            for j in range(1, m): 
                for k in range(j+1):
                    dp[i][j] += dp[i-1][k] 
        return sum(dp[-1])
    
if __name__ == "__main__": 
    s = Solution()
    
    assert s.countVowelStrings(2) == 15  
