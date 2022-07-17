from typing import * 

class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        def check(n, numsDivide):
            for d in numsDivide:
                if d % n != 0:
                    return False 
            return True 
        ans = 0 
        nums.sort()
        i = 0 
        while i < len(nums): 
            n = nums[i]
            if not check(n, numsDivide):
                ans += 1 
                i += 1 
                while i < len(nums): 
                    if nums[i] == n:
                        ans += 1 
                        i += 1 
                    else:
                        break 
            else:
                break 
        if i == len(nums):
            return -1 
        return ans  

if __name__ == "__main__": 
    s = Solution()

    nums = [2,3,2,4,3]
    numsDivide = [9,6,9,3,15]
    assert s.minOperations(nums, numsDivide) == 2

    nums = [4,3,6]
    numsDivide = [8,2,6,10]
    assert s.minOperations(nums, numsDivide) == -1 