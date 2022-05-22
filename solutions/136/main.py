from typing import List 

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for n in nums:
            result ^= n
        return result

if __name__ == "__main__":
    nums = [2,2,1]
    s = Solution()
    assert s.singleNumber(nums) == 1
