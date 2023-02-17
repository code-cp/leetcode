from typing import * 

class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        def gcd(a, b):
            # assum a > b 
            if b == 0: 
                return a 
            return gcd(b, a%b)
        
        g = nums[0]
        for n in nums: 
            g = gcd(n, g)

        return g == 1

if __name__ == "__main__": 
    s = Solution() 

    nums = [12,5,7,23]
    assert s.isGoodArray(nums)