from typing import * 

class Solution:
    def captureForts(self, forts: List[int]) -> int:
        ans = 0 
        n = len(forts)
        
        def countForts():
            nonlocal n 
            nonlocal forts 
            nonlocal ans 
            
            j = None 
            for i in range(n): 
                if j is None and forts[i] != 1:
                    continue 
                if j is None: 
                    j = i 
                    cur = 0 
                    continue 
                if forts[i] == 0: 
                    cur += 1 
                    continue 
                if forts[i] == -1:
                    j = None 
                    ans = max(ans, cur)
                else: 
                    # forts[i] == 1 
                    j = i
                    cur = 0  
                
        countForts()
        forts.reverse()
        countForts()
        
        return ans 
    
if __name__ == "__main__": 
    s = Solution()
    
    # assert s.captureForts([1,0,0,-1,0,0,0,0,1]) == 4 
    assert s.captureForts([-1,-1,-1,-1,1,-1,0,1,1,-1,1,-1]) == 1
    assert s.captureForts([-1,-1,0,1,0,0,1,-1,1,0]) == 1

    
            
            