from typing import * 
from collections import Counter 
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        ans = -1
        max_val = 0  
        for k, v in cnt.items(): 
            if k % 2 != 0: 
                continue 
            if v == max_val and k < ans:
                ans = k 
                continue 
            if v > max_val: 
                ans = k 
                max_val = v 
        return ans  
                