from typing import *

class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        result = ""
        result += str(nums[0])
        if len(nums) == 1: 
            return result 
        result += "/"
        if len(nums) == 2: 
            result += str(nums[1])
            return result
        result += "("
        for i in range(1, len(nums)): 
            result += str(nums[i])
            if i != len(nums)-1:
                result += "/"
            else: 
                result += ")"
        return result 

if __name__ == "__main__": 
    nums = [1000,100,10,2]
    s = Solution()
    assert s.optimalDivision(nums) == "1000/(100/10/2)"