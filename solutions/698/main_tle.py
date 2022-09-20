from typing import * 
from functools import lru_cache

# The time complexity O(2^(k*n)), 
# because if we have K trees stacked on top of each other, 
# the new height of the tree is K * n.
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False 
        nums.sort(reverse=True)
        target = total // k 
        if nums[-1] > target: 
            return False 
        used = 1 << len(nums)

        @lru_cache
        def backtrack(used, start_id, k, sub_sum): 
            # base case 
            if k == 0: 
                return True 
            if sub_sum == target: 
                return backtrack(used, 0, k-1, 0)
            # recurse 
            for i in range(start_id, len(nums)):
                if used & 1 << i or sub_sum+nums[i] > target: 
                    continue 
                if backtrack(used | 1 << i, start_id+1, k, sub_sum+nums[i]):
                    return True 
            return False 

        return backtrack(used, 0, k, 0)

if __name__ == "__main__": 
    s = Solution()

    nums = [2,2,2,2,3,4,5]
    k = 4
    assert not s.canPartitionKSubsets(nums, k)

    nums = [4,3,2,3,5,2,1]
    k = 4
    assert s.canPartitionKSubsets(nums, k)