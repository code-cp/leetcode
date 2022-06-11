class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        # dp table 
        dp = [[0] * 2 for _ in range(len(s))]
        # init dp 
        dp[0][0] = int(s[0])
        dp[0][1] = 1-int(s[0]) 
        # traverse 
        for i in range(1, len(s)): 
            dp[i][0] = dp[i-1][0] + int(s[i])
            dp[i][1] = min(dp[i-1][0], dp[i-1][1]) + 1-int(s[i])
        return min(dp[-1][0], dp[-1][1])

if __name__ == "__main__": 
    sol = Solution() 

    assert sol.minFlipsMonoIncr("010110") == 2 
    assert sol.minFlipsMonoIncr("00011000") == 2 
    assert sol.minFlipsMonoIncr("00110") == 1 