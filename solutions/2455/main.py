from typing import * 

class Solution:
    def averageValue(self, nums: List[int]) -> int:
        ans = 0 
        cnt = 0 
        for n in nums: 
            if n % 6 == 0: 
                ans += n 
                cnt += 1 
        return 0 if cnt == 0 else ans // cnt 