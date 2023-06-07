from typing import * 

class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        avgs = set()
        for i in range(n//2):
            avg = (nums[i]+nums[n-i-1])/2  
            avgs.add(avg)
        return len(avgs)
    
if __name__ == "__main__": 
    s = Solution() 
    
    assert s.distinctAverages([4,1,4,0,3,5]) == 2 