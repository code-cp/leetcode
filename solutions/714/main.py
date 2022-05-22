from typing import List 

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        result = 0
        minPrice = float('inf')
        for p in prices:
            if minPrice > p:
                minPrice = p
            elif p - minPrice > fee:
                result += p - minPrice - fee
                minPrice = p - fee
        return result

if __name__ == "__main__":
    prices = [1,3,2,8,4,9]
    fee = 2 
    s = Solution()
    assert s.maxProfit(prices, fee) == 8
