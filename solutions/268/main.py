from typing import List 

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # think of the array as newArray = nums + [0...n]
        # so each number show up twice except the missing one
        # ref https://tenderleo.gitbooks.io/leetcode-solutions-/content/GoogleMedium/268.html
        result = 0
        for i in range(len(nums)):
            result ^= nums[i] ^ (i+1)
        return result

if __name__ == "__main__":
    s = Solution()
    nums = [3,0,1]
    assert s.missingNumber(nums) == 2
