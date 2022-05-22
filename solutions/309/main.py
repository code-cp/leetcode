from typing import List 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp table
        # case 0, no stock, not CD
        # case 1, no stock, sell today
        # case 2, CD
        # case 3, hold stock
        dp = [[0] * 4 for _ in range(len(prices))]
        # initialize
        dp[0][3] = -prices[0]
        # traverse dp table
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][2])
            dp[i][1] = dp[i-1][3] + prices[i]
            dp[i][2] = dp[i-1][1]
            dp[i][3] = max(dp[i-1][3], max(dp[i-1][0] - prices[i], dp[i-1][2] - prices[i]))
        return max(*dp[-1][:-1])

if __name__ == "__main__":
    prices = [1,2,3,0,2]
    s = Solution()
    assert s.maxProfit(prices) == 3
