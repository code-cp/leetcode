from typing import List 

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_val = max(nums)
        max_id = nums.index(max_val)
        for n in nums: 
            if max_val < 2*n and max_val != n: 
                return -1 
        return max_id

if __name__ == "__main__": 
    nums = [3,6,1,0]
    s = Solution()
    assert s.dominantIndex(nums) == 1
