from typing import * 

def memoize(function):
  memo = {}
  def wrapper(*args):
    if args in memo:
      return memo[args]
    else:
      rv = function(*args)
      memo[args] = rv
      return rv
  return wrapper

# time complexity O(2^kn)
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k:
            return False
        target = total // k
        nums.sort()  
        if nums[-1] > target:
            return False
        n = len(nums)

        @memoize
        def backtrack(used, cur_sum):
            if used+1 == 1<<(n+1):
                return True
            for i in range(n):
                if nums[i] + cur_sum > target:
                    # since nums is sorted 
                    # no need to use larger values 
                    break
                if used >> i & 1:
                    continue 
                if backtrack(used | (1 << i), (cur_sum + nums[i]) % target):  
                    return True
            return False

        return backtrack(1 << n, 0)


if __name__ == "__main__": 
    s = Solution()

    nums = [2,2,2,2,3,4,5]
    k = 4
    assert not s.canPartitionKSubsets(nums, k)

    nums = [4,3,2,3,5,2,1]
    k = 4
    assert s.canPartitionKSubsets(nums, k)