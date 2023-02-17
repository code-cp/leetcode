from typing import * 

from collections import Counter 
class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        ans = [0]*2
        for k, v in cnt.items(): 
            ans[0] += v//2 
            ans[1] += v%2 
        return ans 