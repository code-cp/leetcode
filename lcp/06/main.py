from typing import * 

class Solution:
    def minCount(self, coins: List[int]) -> int:
        ans = 0 
        for c in coins: 
            ans += (c+1)//2 
        return ans 