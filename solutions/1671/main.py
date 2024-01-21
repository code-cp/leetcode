from typing import * 

class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        # init dp 
        left = [1]*n 
        right = [1]*n
        
        # longest increasing subarray starting from left 
        for i in range(n):
            for j in range(i): 
                if nums[j] < nums[i]:  
                    left[i] = max(left[i], left[j]+1)
        # longest increasing subarray starting from right 
        for i in range(n-1, -1, -1): 
            for j in range(n-1, i, -1):
                if nums[j] < nums[i]: 
                    right[i] = max(right[i], right[j]+1)
                    
        ans = 0
        # NOTE, 0 < i < arr.length - 1 
        for i in range(1, n-1): 
            # NOTE, arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
            # arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
            if left[i] < 2 or right[i] < 2: 
                continue 
            ans = max(ans, left[i]+right[i]-1)
            
        return n-ans 
    
if __name__ == "__main__": 
    s = Solution()
    
    assert s.minimumMountainRemovals([100,92,89,77,74,66,64,66,64]) == 6 
    assert s.minimumMountainRemovals([9,8,1,7,6,5,4,3,2,1]) == 2  