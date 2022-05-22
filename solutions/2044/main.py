from typing import *  

class Solution:
    def backtracking(self, nums, cur_value, start_idx):
        # base case 
        # NOTE: no need to check if start_idx == len(nums)
        if cur_value > self.max_value:
            self.max_value = cur_value
            self.count = 1 
            if self.debug_mode: 
                self.ans = [[nums[x] for x in self.ids]]
        elif cur_value == self.max_value: 
            self.count += 1 
            if self.debug_mode: 
                self.ans.append([nums[x] for x in self.ids])

        # backtracking
        for i in range(start_idx, len(nums)):
            if self.debug_mode: 
                self.ids.append(i)
            self.backtracking(nums, cur_value | nums[i], i+1)
            if self.debug_mode: 
                self.ids.pop()

    def countMaxOrSubsets(self, nums: List[int]) -> int:
        self.count = 0 
        self.max_value = 0 
        self.debug_mode = False  
        if self.debug_mode: 
            self.ids = []
            self.ans = []
        self.backtracking(nums, 0, 0)
        return self.count 

if __name__ == "__main__": 
    s = Solution()

    nums = [3,1]
    assert s.countMaxOrSubsets(nums) == 2 

    nums = [2,2,2]
    assert s.countMaxOrSubsets(nums) == 7 

    nums = [3,2,1,5]
    assert s.countMaxOrSubsets(nums) == 6