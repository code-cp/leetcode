from typing import * 

class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        M = 1e9 + 7
        res = 0 
        nums.sort()
        n = len(nums)
        pow2 = [0]*n 
        pow2[0] = 1 
        for i in range(1, n): 
            pow2[i] = pow2[i-1]*2%M
        for i in range(n): 
            res += (nums[i]*(pow2[i]-pow2[n-1-i]))%M
            res %= M 
        return int(res%M)

if __name__ == "__main__": 
    s = Solution() 

    nums = [5,69,89,92,31,16,25,45,63,40,16,56,24,40,75,82,40,12,50,62,92,44,67,38,92,22,91,24,26,21,100,42,23,56,64,43,95,76,84,79,89,4,16,94,16,77,92,9,30,13]
    assert s.sumSubseqWidths(nums) == 857876214 

    nums = [2,1,3]
    assert s.sumSubseqWidths(nums) == 6 
