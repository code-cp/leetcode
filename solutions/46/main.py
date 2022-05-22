from typing import List 

class Solution:
    def __init__(self):
        self.path = []
        self.result = []
    def backtracking(self, nums):
        # base case
        if (len(self.path) == len(nums)):
            self.result.append(self.path[:])
            return
        for i in range(len(nums)):
            if nums[i] in self.path:
                continue
            self.path.append(nums[i])
            self.backtracking(nums)
            self.path.pop()
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.backtracking(nums)
        return self.result

if __name__ == "__main__":
    s = Solution()
    nums = [1,2,3]
    print(s.permute(nums))
