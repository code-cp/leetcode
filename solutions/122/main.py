from typing import List 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curMin = float('inf')
        result = 0
        for i in range(len(prices)):
            if prices[i] < curMin:
                curMin = prices[i]
            if prices[i] > curMin:
                result += prices[i] - curMin
                curMin = prices[i]
        return result

if __name__ == "__main__":
    mySol = Solution()
    prices = [7,1,5,3,6,4]
    assert mySol.maxProfit(prices) == 7
