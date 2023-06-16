from typing import * 

class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        def checkBits(n, num): 
            i = 0 
            while i < n:
                if ((num >> i) & 1) != 0:
                    break 
                i += 1 
            while i < n: 
                if ((num >> i) & 1) != 1: 
                    return False 
                i += 1 
            return True  
                
             
        ans = 0 
        num = 0 
        n = max(flips)
        for f in flips: 
            num |= 1 << (n-f)
            if checkBits(n, num):
                ans += 1 
        return ans 
    
if __name__ == "__main__": 
    s = Solution() 
    
    assert s.numTimesAllBlue([3,2,4,1,5]) == 2 
            
         
        