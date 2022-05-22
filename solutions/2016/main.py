from typing import * 

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        max_val = -1
        min_val = float("inf")

        for n in nums: 
            if n < min_val:
                min_val = n 
            if n > min_val: 
                diff = n - min_val
                if diff > max_val: 
                    max_val = diff 

        return max_val 

if __name__ == "__main__": 
    s = Solution()
    nums = [7,1,5,4]
    assert s.maximumDifference(nums) == 4 