class Solution:
    def countVowelPermutation(self, n: int) -> int:
        # dp table 
        dp = [[0] * 5 for _ in range(n)]
        # initialize 
        for i in range(5): 
            dp[0][i] = 1 
        # traverse dp 
        for i in range(1, n):
            dp[i][0] = dp[i-1][1] + dp[i-1][2] + dp[i-1][4]
            dp[i][1] = dp[i-1][0] + dp[i-1][2]
            dp[i][2] = dp[i-1][1] + dp[i-1][3] 
            dp[i][3] = dp[i-1][2]
            dp[i][4] = dp[i-1][2] + dp[i-1][3]
        return sum(dp[-1]) % (pow(10, 9) + 7)

if __name__ == "__main__": 
    n = 5
    s = Solution()
    assert s.countVowelPermutation(n) == 68
