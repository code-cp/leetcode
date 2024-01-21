from typing import * 

# 一张桌子上有n件商品围成一圈，每件都有一个价签，它们构成数组nums。除了按照价签上的价格买东西之外，
# 你还可以花x块钱把桌子转一下，把每件商品都对应到下一个价签，问把每种商品买一遍最少花多少钱

class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        ans = float("inf") 
        min_prices = [n for n in nums]
        n = len(nums)
        # in range(n), not range(1, n)
        # since we may not rotate at all 
        # and collect at original prices 
        for i in range(n):
            # [0,1,2] -> [1,2,0]
            new_prices = nums[-i:] + nums[:n-i]
            for j in range(n): 
                min_prices[j] = min(min_prices[j], new_prices[j])             
            cost = sum(min_prices) + i * x 
            ans = min(ans, cost)    
        return ans 
    
if __name__ == "__main__": 
    s = Solution()
    
    # assert s.minCost([20,1,15], 5) == 13
    assert s.minCost([1,2,3], 4) == 6 