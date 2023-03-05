from typing import * 

import math
class Solution:
    def findValidSplit(self, nums: List[int]) -> int:
        n = len(nums)

        prefix = []
        mul = 1 
        for i in range(n-1): 
            mul *= nums[i]
            prefix.append(mul)

        sufix = []
        mul = 1 
        for i in range(n-1, 0, -1): 
            mul *= nums[i]
            sufix.append(mul)

        for i in range(n-1): 
            p = prefix[i]
            s = sufix[n-2-i]
            if math.gcd(p, s) == 1: 
                return i 

        return -1 
        

if __name__ == "__main__": 
    s = Solution() 

    nums = [4,7,15,8,3,5]
    assert s.findValidSplit(nums) == -1 

    # nums = [4,7,8,15,3,5]
    # assert s.findValidSplit(nums) == 2 

