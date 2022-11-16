from typing import * 

class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        n = len(nums)
        max_val = -1 
        for i in range(n-2): 
            max_val = max(max_val, nums[i])
            if max_val > nums[i+2]: 
                return False 
        return True 

if __name__ == "__main__": 
    s = Solution()

    nums = [1,3,2,0]
    assert not s.isIdealPermutation(nums) 

    nums = [1,2,0]
    assert not s.isIdealPermutation(nums) 

    nums = [1,0,2]
    assert s.isIdealPermutation(nums) 