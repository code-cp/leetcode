from typing import List 

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # check input
        if len(prices) == 0:
            return 0
        # dp table
        dp = [[0] * (2*k + 1) for _ in range(len(prices))]
        # initialize
        for i in range(1, 2*k + 1, 2):
            dp[0][i] = -prices[0]
        # traverse
        for i in range(1, len(prices)):
            for j in range(2*k + 1):
                if j == 0:
                    dp[i][0] = dp[i-1][0]
                elif j % 2 == 1:
                    dp[i][j] = max(dp[i-1][j-1] - prices[i], dp[i-1][j])
                else:
                    dp[i][j] = max(dp[i-1][j-1] + prices[i], dp[i-1][j])
        return dp[-1][-1]

if __name__ == "__main__":
    k = 2 
    prices = [3,2,6,5,0,3]
    s = Solution()
    assert s.maxProfit(k, prices) == 7
