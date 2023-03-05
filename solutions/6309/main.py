from typing import * 

class Solution:
    def findValidSplit(self, nums: List[int]) -> int:        
        n = len(nums)
        first_pos = {}
        # right most position for i is at least i 
        right_pos = [i for i in range(n)]
        
        def update(p, i):
            if first_pos.get(p, -1) == -1: 
                # first time p appears 
                first_pos[p] = i
            else:  
                right_pos[first_pos[p]] = i
        
        for i, x in enumerate(nums): 
            fac = 2 
            while fac**2 <= x: 
                if x%fac == 0: 
                    update(fac, i)
                    while x%fac == 0: 
                        x //= fac 
                fac += 1 
            if x > 1: 
                update(x, i)
        
        i = 0 
        right = 0 
        while i <= right: 
            right = max(right, right_pos[i])
            i += 1 
            
        return right if right < n-1 else -1 
            


if __name__ == "__main__": 
    s = Solution() 

    nums = [4,7,15,8,3,5]
    assert s.findValidSplit(nums) == -1 

    nums = [4,7,8,15,3,5]
    assert s.findValidSplit(nums) == 2 

