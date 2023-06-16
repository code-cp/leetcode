from typing import * 

class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:             
        ans = right_most = 0 
        for i, flip in enumerate(flips): 
            right_most = max(right_most, flips[i])
            if right_most == i+1: 
                ans += 1 
        return ans 
    
if __name__ == "__main__": 
    s = Solution() 
    
    assert s.numTimesAllBlue([3,2,4,1,5]) == 2 
            
         
        