from typing import * 

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # ref https://leetcode.cn/problems/find-peak-element/solutions/998152/xun-zhao-feng-zhi-by-leetcode-solution-96sj/?envType=daily-question&envId=2023-12-18
        
        n = len(nums)
        if n == 1: 
            return 0
        
        def checkPeak(ind):
            nonlocal nums 
            nonlocal n  
            if ind == 0 and nums[ind] > nums[ind+1]: 
                return True 
            if ind == n-1 and nums[ind] > nums[ind-1]: 
                return True 
            if nums[ind-1] < nums[ind] and nums[ind] > nums[ind+1]:
                return True 
            return False  
        
        l, r = 0, n-1
        while l <= r: 
            # NOTE, use () for >> 
            mid = ((r-l) >> 1) + l 
            if checkPeak(mid): 
                return mid 
            if nums[mid] < nums[mid+1]: 
                l = mid + 1 
            else: 
                r = mid - 1 
       
if __name__ == "__main__": 
    s = Solution()
    
    assert s.findPeakElement([1,2,3,1]) == 2 