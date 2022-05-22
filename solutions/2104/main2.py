from typing import * 
from collections import deque 

class Solution:
    def getMax(self, nums, reverse=False): 
        stack = deque()
        n = len(nums)

        if not reverse:
            result = [n] * n
            for i in range(n):
                while len(stack) and nums[i] >= nums[stack[-1]]: 
                    idx = stack.pop()
                    result[idx] = i 
                stack.append(i)
        else:
            result = [-1] * n
            for i in range(n-1, -1, -1):
                while len(stack) and nums[i] > nums[stack[-1]]: 
                    idx = stack.pop()
                    result[idx] = i 
                stack.append(i)

        return result 

    def getMin(self, nums, reverse=False): 
        stack = deque()
        n = len(nums)

        if not reverse:
            result = [n] * n
            for i in range(n):
                while len(stack) and nums[i] < nums[stack[-1]]: 
                    idx = stack.pop()
                    result[idx] = i 
                stack.append(i)
        else: 
            result = [-1] * n
            for i in range(n-1, -1, -1):
                while len(stack) and nums[i] <= nums[stack[-1]]: 
                    idx = stack.pop()
                    result[idx] = i 
                stack.append(i)

        return result 

    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)

        right_max_val = self.getMax(nums)
        right_min_val = self.getMin(nums)

        left_max_val = self.getMax(nums, reverse=True)
        left_min_val = self.getMin(nums, reverse=True)

        result = 0 
        for i in range(n):
            right_max_num = max(right_max_val[i] - i, 1) 
            left_max_num = max(i - left_max_val[i], 1) 
            max_total = right_max_num * left_max_num 

            right_min_num = max(right_min_val[i] - i, 1) 
            left_min_num = max(i - left_min_val[i], 1) 
            min_total = right_min_num * left_min_num 

            result += (max_total - min_total) * nums[i]
        return result 

if __name__ == "__main__": 
    s = Solution()

    nums = [1,2,3]
    result = s.subArrayRanges(nums)
    assert result == 4 

    nums = [3,3]
    result = s.subArrayRanges(nums)
    assert result == 0

    nums = [1,3,3]
    result = s.subArrayRanges(nums)
    assert result == 4 