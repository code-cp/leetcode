from typing import List 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp table 
        # 0 = no action 
        # 1 = 1st buy 
        # 2 = 1st sell 
        # 3 = 2nd buy 
        # 4 = 2nd sell 
        dp = [[0] * 5 for _ in range(len(prices))]
        # initialize 
        dp[0][0] = 0 
        dp[0][1] = -prices[0]
        dp[0][2] = 0 
        dp[0][3] = -prices[0]
        dp[0][4] = 0 
        # traverse 
        for i in range(1, len(prices)): 
            dp[i][0] = dp[i-1][0]
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
            dp[i][2] = max(dp[i-1][2], dp[i-1][1] + prices[i])
            dp[i][3] = max(dp[i-1][3], dp[i-1][2] - prices[i])
            dp[i][4] = max(dp[i-1][4], dp[i-1][3] + prices[i])
        return max(dp[-1][2], dp[-1][-1])
        
if __name__ == "__main__": 
    prices = [7,6,4,3,1]
    s = Solution()
    assert s.maxProfit(prices) == 0
