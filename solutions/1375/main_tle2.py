from typing import * 

class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:             
        ans = 0 
        num = 0 
        for i, f in enumerate(flips): 
            num |= (1 << (f-1)) 
            if num == 2**(i+1)-1:
                ans += 1 
        return ans 
    
if __name__ == "__main__": 
    s = Solution() 
    
    assert s.numTimesAllBlue([3,2,4,1,5]) == 2 
            
         
        