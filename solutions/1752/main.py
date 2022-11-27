from typing import * 

class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        nums.extend(nums)

        def checkArray(arr, start_idx):
            for i in range(start_idx+1, start_idx+n): 
                if arr[i] < arr[i-1]: 
                    return False 
            return True 
        
        for start_idx in range(n): 
            if checkArray(nums, start_idx):
                return True 

        return False 

if __name__ == "__main__": 
    s = Solution() 

    nums = [3,4,5,1,2]
    assert s.check(nums)

    nums = [2,1,3,4]
    assert not s.check(nums)