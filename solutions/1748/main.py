from typing import List 
from collections import defaultdict

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        nums_dict = defaultdict(int)
        for n in nums:
            nums_dict[n] += 1 
        result = 0
        for m, n in nums_dict.items():
            if n == 1: 
                result += m
        return result  

if __name__ == "__main__": 
    nums = [1,2,3,2]
    s = Solution()
    assert s.sumOfUnique(nums) == 4 