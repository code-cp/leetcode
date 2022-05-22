from collections import defaultdict
from typing import List 

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        result = 0 
        nums_dict = defaultdict(int)
        for n in nums: 
            if n in nums_dict:
                result += nums_dict[n]
            nums_dict[n+k] += 1 
            nums_dict[n-k] += 1 
        return result 

if __name__ == "__main__": 
    nums = [1,2,2,1]
    k = 1 
    s = Solution()
    assert s.countKDifference(nums, k) == 4