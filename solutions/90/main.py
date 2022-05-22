from typing import List

class Solution:
    def __init__(self): 
        self.path = []
        self.result = []
    def backtracking(self, nums, startId): 
        # collect all nodes 
        self.result.append(self.path[:])
        # base case 
        if startId == len(nums): 
            return 
        for i in range(startId, len(nums)):
            if i > startId and nums[i] == nums[i-1]:
                continue 
            self.path.append(nums[i])
            self.backtracking(nums, i+1)
            self.path.pop()
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        self.backtracking(nums, 0)
        return self.result 

if __name__ == "__main__":
    s = Solution()
    nums = [1,2,2]
    print(s.subsetsWithDup(nums))
