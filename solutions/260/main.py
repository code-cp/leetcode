from typing import List 

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        result = [0, 0]
        diff = 0
        for n in nums:
            diff ^= n
        diff = diff & -diff
        for n in nums:
            if n & diff:
                result[0] ^= n
            else:
                result[1] ^= n
        return result

if __name__ == "__main__":
    nums = [1,2,1,3,2,5]
    s = Solution()
    print(s.singleNumber(nums))
