from typing import * 

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        first, second = 0, 0 
        while first < len(nums) and second < len(nums):
            if nums[first] % 2 == 1: 
                while second < len(nums) and (nums[second] % 2 == 1 or second <= first):
                    second += 1 
                if second < len(nums):
                    nums[first], nums[second] = nums[second], nums[first]
                    first += 1
                    second += 1
            else: 
                first += 1 
        return nums 

if __name__ == "__main__": 
    s = Solution() 

    nums = [1]
    result = s.sortArrayByParity(nums)
    assert result == [1] 

    nums = [0]
    result = s.sortArrayByParity(nums)
    assert result == [0] 

    nums = [3,1,2,4]
    result = s.sortArrayByParity(nums)
    assert result == [2,4,3,1] 