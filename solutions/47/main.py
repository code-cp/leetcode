from typing import List 

class Solution:
    def __init__(self):
        self.path = []
        self.result = []
    def backtracking(self, nums, used):
        # base case
        if len(self.path) == len(nums):
            self.result.append(self.path[:])
            return
        uset = []
        for i in range(0, len(nums)):
            # avoid duplicates in the same level
            if nums[i] in uset:
                continue
            # avoid duplicates of same element
            if used[i]:
                continue
            uset.append(nums[i])
            used[i] = 1
            self.path.append(nums[i])
            self.backtracking(nums, used)
            self.path.pop()
            used[i] = 0
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        used = [0] * len(nums)
        self.backtracking(nums, used)
        return self.result

if __name__ == "__main__":
    s = Solution()
    nums = [1,1,2]
    print(s.permuteUnique(nums))
