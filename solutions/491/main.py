from typing import List

class Solution:
    def __init__(self): 
        self.path = []
        self.result = []
    def backtracking(self, nums, startId): 
        # collect all nodes 
        if len(self.path) > 1: 
            self.result.append(self.path[:])
        # base case 
        if startId == len(nums): 
            return 
        usedSameLevel = []
        for i in range(startId, len(nums)):
            if (len(self.path) > 0 and nums[i] < self.path[-1]):
                continue 
            if nums[i] in usedSameLevel: 
                continue 
            usedSameLevel.append(nums[i])
            self.path.append(nums[i])
            self.backtracking(nums, i+1)
            self.path.pop()
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.backtracking(nums, 0)
        return self.result 

if __name__ == "__main__":
    s = Solution()
    nums = [4,6,7,7]
    print(s.findSubsequences(nums))
