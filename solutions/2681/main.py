from typing import * 

class Solution:
    def sumOfPower(self, nums: List[int]) -> int:
        ans = 0 
        M = 10**9 + 7
        nums.sort()
        
        total = 0
        for i, n in enumerate(nums): 
            if i > 0: 
                total = (total * 2 + nums[i-1]) % M     
            ans += (total * n**2 + n**3) % M 
            ans %= M 
            
        return ans 