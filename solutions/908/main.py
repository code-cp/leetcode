from typing import *

class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        return max(0, max(nums) - min(nums) - 2 * k) 

if __name__ == "__main__": 
    s = Solution()

    assert s.smallestRangeI([1], 0) == 0 
    assert s.smallestRangeI([0,10], 2) == 6 