from typing import * 

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()
        cnt = 0 
        i = 0 
        n = len(nums)
        m = 0 
        while i < n:
            while i < n and nums[i] == m: 
                i += 1 
            if i < n: 
                nums[i] -= m 
                m += nums[i]
                cnt += 1 
                i += 1 
        return cnt 

if __name__ == "__main__": 
    s = Solution() 
    
    nums = [1,5,0,3,5]
    assert s.minimumOperations(nums) == 3 