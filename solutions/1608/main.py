from typing import * 
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        def bsearch(nums, target): 
            l, r = 0, n-1 
            while l <= r: 
                mid = (r-l)//2+l 
                if nums[mid] < target: 
                    l = mid+1 
                else: 
                    r = mid-1 
            return l 

        for i in range(1, n+1): 
            j = bsearch(nums, i)
            if n-j == i: 
                return i 

        return -1 

if __name__ == "__main__": 
    s = Solution()

    nums = [0,4,3,0,4]
    assert s.specialArray(nums) == 3 