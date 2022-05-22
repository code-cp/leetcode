class Solution:
    def __init__(self): 
        self.path = []
        self.result = []
    def backtracking(self, nums, startId): 
        # collect node 
        self.result.append(self.path[:])
        # base case 
        if startId == len(nums):
            return 
        for i in range(startId, len(nums)):
            self.path.append(nums[i])
            self.backtracking(nums, i+1)
            self.path.pop()
    def subsets(self, nums):
        self.backtracking(nums, 0)
        return self.result 

if __name__ == "__main__":
    s = Solution()
    nums = [1,2,3]
    print(s.subsets(nums))
