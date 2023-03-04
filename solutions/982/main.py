from typing import * 

class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        M = max(nums)
        cnt = [0]*(M+1)
        for i in nums: 
            for j in nums: 
                # AND can only decrease the number 
                cnt[i&j] += 1  
        res = 0 
        for k in nums:
            for m in range(M+1):  
                if (k&m) == 0:
                    res += cnt[m]
        return res 


