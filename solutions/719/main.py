from typing import * 

# wrong 
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        t = k 
        m = 0
        n = len(nums)-1
        while t > 0: 
            k = t 
            t -= n
            m += 1
            n -= 1   
        k -= 1 
        diff = [nums[i] - nums[i-m] for i, _ in enumerate(nums) if i >= m]
        diff.sort()
        return diff[k]

if __name__ == "__main__": 
    s = Solution()

    assert s.smallestDistancePair([1,3,1], 1) == 0

    # assert s.smallestDistancePair([1,1,1], 2) == 0

    # assert s.smallestDistancePair([1,6,1], 3) == 5

    assert s.smallestDistancePair([9,10,7,10,6,1,5,4,9,8], 18) == 2