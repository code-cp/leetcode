from typing import List 

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # dp table
        dp = [[0] * 2 for _ in range(len(prices))]
        # initialize
        dp[0][1] = -prices[0]
        # traverse dp table
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i] - fee)
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
        return dp[-1][0]

if __name__ == "__main__":
    prices = [1,3,2,8,4,9]
    fee = 2 
    s = Solution()
    assert s.maxProfit(prices, fee) == 8
