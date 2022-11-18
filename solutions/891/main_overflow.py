from typing import * 

class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        M = 1e9 + 7
        res = 0 
        nums.sort()
        n = len(nums)
        for i in range(n): 
            # int too large to convert to float
            res -= ((nums[i]%M)*(2**(n-1-i))%M)%M
            res += ((nums[i]%M)*(2**i)%M)%M
            res %= M 
        return int(res%M)

if __name__ == "__main__": 
    s = Solution() 

    nums = [2,1,3]
    assert s.sumSubseqWidths(nums) == 6 
