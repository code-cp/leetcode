from typing import List 

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # dp table
        # dp[i][j] means no. of sub of t[0:i-1] for s[0:j-1]
        dp = [[0] * (len(t)+1) for _ in range(len(s)+1)]
        # initialize
        for i in range(1, len(t)+1):
            dp[0][i] = 0
        for i in range(1, len(s)+1):
            dp[i][0] = 1
        dp[0][0] = 1
        # traverse dp table
        for i in range(1, len(s)+1):
            for j in range(1, len(t)+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]

if __name__ == "__main__": 
    s = "rabbbit"
    t = "rabbit"
    sol = Solution()
    assert sol.numDistinct(s, t) == 3
