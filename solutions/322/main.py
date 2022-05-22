from typing import List 

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp table
        MAX = amount + 1
        dp = [[MAX] * (amount+1) for _ in range(len(coins)+1)]
        # initialize
        dp[0][0] = 0
        for i in range(1, len(coins)+1):
            # note, this is NOT for j in range(1, amount+1):
            for j in range(amount+1):
                if j < coins[i-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-coins[i-1]] + 1)
        return dp[-1][-1] if dp[-1][-1] < MAX else -1

if __name__ == "__main__":
    coins = [1,2,5] 
    amount = 11
    s = Solution()
    assert s.coinChange(coins, amount) == 3
