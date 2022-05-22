from typing import List 

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp table
        dp = [[0] * (len(coins)+1) for _ in range(amount+1)]

        # initialize
        for i in range(len(coins)+1):
            dp[0][i] = 1

        for i in range(1, amount+1):
            for j in range(1, len(coins)+1):
                if i < coins[j-1]:
                    dp[i][j] = dp[i][j-1]
                else:
                    dp[i][j] = dp[i][j-1] + dp[i-coins[j-1]][j]

        return dp[-1][-1]

if __name__ == "__main__":
    coins = [1,2,5]
    amount = 5
    s = Solution()
    assert s.change(amount, coins) == 4
