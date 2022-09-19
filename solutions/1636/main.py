from typing import * 

from collections import Counter
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        # -x: If multiple values have the same frequency, sort them in decreasing order 
        nums.sort(key=lambda x: (cnt[x], -x))
        return nums 


if __name__ == "__main__": 
    s = Solution()

    nums = [1,1,2,2,2,3]
    assert s.frequencySort(nums) == [3,1,1,2,2,2]
