from typing import * 

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        dp = [[0]*2 for _ in range(len(flowerbed))] 
        for i, f in enumerate(flowerbed):
            if i == 0: 
                if f == 0:
                    dp[i][1] = 1 
                else: 
                    dp[i][0] = -float("inf")
                continue 
        
            if f == 0:
                dp[i][0] = max(dp[i-1][0], dp[i-1][1])
                # NOTE, need to check the positions afterward 
                if i <= len(flowerbed)-2 and flowerbed[i+1] == 1:
                    # can't place flower here 
                    dp[i][1] = -float("inf")
                else:  
                    dp[i][1] = dp[i-1][0] + 1  
            else: 
                # invaid state 
                dp[i][0] = -float("inf")
                # previous state must be 0 
                dp[i][1] = dp[i-1][0] 
                
        return max(dp[-1][0], dp[-1][1]) >= n 
    
if __name__ == "__main__": 
    s = Solution()
    
    # assert s.canPlaceFlowers([1,0,0,0,1], 1)
    assert s.canPlaceFlowers([1,0,0,0,0,1], 2)