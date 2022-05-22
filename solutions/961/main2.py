from typing import * 

import random 
class Solution:
    def partition(self, nums, left, right): 
        pivot = random.randint(left, right)
        nums[pivot], nums[right] = nums[right], nums[pivot] 
        i = left 
        for j in range(left, right): 
            if nums[j] <= nums[right]: 
                nums[i], nums[j] = nums[j], nums[i] 
                i += 1
                if nums[j] == nums[right]:
                    self.found_n = True 
                    self.n = nums[right]                
        nums[i], nums[right] = nums[right], nums[i] 
        return i 
    def qselect(self, nums, left, right, k): 
        if left == right: 
            return left 
        pivot = self.partition(nums, left, right) 
        if self.found_n: 
            return self.n 
        if pivot == k: 
            return pivot
        elif pivot > k: 
            return self.qselect(nums, left, pivot-1, k) 
        else:
            return self.qselect(nums, pivot+1, right, k) 
    def repeatedNTimes(self, nums: List[int]) -> int:
        self.found_n = False 
        self.n = None 
        ans = self.qselect(nums, 0, len(nums)-1, len(nums)//2)
        if self.found_n: 
            return self.n 
        if ans+1 < len(nums) and nums[ans] == nums[ans+1]:
            return nums[ans+1]
        else: 
            return nums[ans-1]


if __name__ == "__main__": 
    s = Solution()

    assert s.repeatedNTimes([9,5,3,3]) == 3
    assert s.repeatedNTimes([4,1,7,0,0,9,0,0]) == 0
    assert s.repeatedNTimes([5,1,5,2,5,3,5,4]) == 5 