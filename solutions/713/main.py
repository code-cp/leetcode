from typing import * 

# TLE https://leetcode-cn.com/submissions/detail/309445291/
# class Solution:
#     def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
#         res = 0 
#         n = len(nums)
#         for i in range(n-1, -1, -1):
#             product = nums[i]
#             j = i 
#             while product < k and j >= 0: 
#                 j -= 1 
#                 if j >= 0: 
#                     product *= nums[j]
#                 res += 1 
#         return res 

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res = 0 
        n = len(nums)
        product = nums[n-1]
        prev = n-1  
        for i in range(n-1, -1, -1):
            j = prev 
            res += i - j 
            while product < k and j >= 0: 
                j -= 1 
                if j >= 0: 
                    product *= nums[j]
                res += 1 
            if j+1 < i: 
                product /= nums[j]
                prev = j+1
                product /= nums[i]
            else: 
                product = nums[i-1]
                prev = i-1
        return res 


if __name__ == "__main__": 
    s = Solution()

    nums = [57,44,92,28,66,60,37,33,52,38,29,76,8,75,22]
    k = 18
    result = s.numSubarrayProductLessThanK(nums, k)
    assert result == 1

    nums = [1,1,1]
    k = 1
    result = s.numSubarrayProductLessThanK(nums, k)
    assert result == 0

    nums = [1,2,3]
    k = 0
    result = s.numSubarrayProductLessThanK(nums, k)
    assert result == 0 

    nums = [10,5,2,6]
    k = 100
    result = s.numSubarrayProductLessThanK(nums, k)
    assert result == 8 