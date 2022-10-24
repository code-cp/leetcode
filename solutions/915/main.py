from typing import * 

class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        n = len(nums)
        max_arr = [0] * n 
        min_arr = [0] * n
        
        max_val = -1 
        for i in range(n): 
            max_arr[i] = max(nums[i], max_val) 
            max_val = max_arr[i]
        
        min_val = float("inf")
        for i in range(n-1, -1, -1): 
            min_arr[i] = min(nums[i], min_val)
            min_val = min_arr[i]

        for i in range(n-1):
            if max_arr[i] <= min_arr[i+1]: 
                return i+1

if __name__ == "__main__": 
    s = Solution() 

    nums = [1,1]
    assert s.partitionDisjoint(nums) == 1 

    nums = [5,0,3,8,6]
    assert s.partitionDisjoint(nums) == 3 

