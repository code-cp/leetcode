from typing import * 

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i, n in enumerate(nums): 
            if i+1 == len(nums): 
                continue 
            if nums[i] == nums[i+1]: 
                if nums[i] == 0: 
                    continue 
                nums[i] *= 2 
                nums[i+1] = 0 
        
        i = j = 0 
        n = len(nums)
        while True: 
            while i < n and nums[i] != 0: 
                i += 1 
            j = i 
            while j < n and nums[j] == 0: 
                j += 1 
            if i == n or j == n: 
                break 
            nums[i], nums[j] = nums[j], nums[i]
            
        return nums 
    
if __name__ == "__main__": 
    s = Solution() 
    
    # assert s.applyOperations([1,2,2,1,1,0]) == [1,4,2,0,0,0]
    assert s.applyOperations([0,1]) == [1,0]