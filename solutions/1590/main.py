from typing import * 

# ref https://leetcode.cn/problems/make-sum-divisible-by-p/solutions/2158435/tao-lu-qian-zhui-he-ha-xi-biao-pythonjav-rzl0/

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        rem = sum(nums) % p
        if rem == 0: 
            return 0 
        
        n = len(nums)
        
        # Use a map to keep track of the rightmost index for every prefix sum % p
        # this is because when we iterate, we need to find the index most close to cur idx 
        res = n 
        prefix = 0 
        # NOTE, idx starts from -1 
        right = {prefix: -1}  
        for i in range(n): 
            prefix += nums[i]
            # NOTE, do NOT construct right in a separate loop 
            right[prefix%p] = i 
            j = right.get((prefix-rem)%p, -n)
            res = min(res, i-j)
            
        return res if res < n else -1 
    
if __name__ == "__main__": 
    s = Solution() 

    nums = [3,1,4,2]
    p = 6
    assert s.minSubarray(nums, p) == 1
    
    nums = [6,3,5,2]
    p = 9
    assert s.minSubarray(nums, p) == 2  