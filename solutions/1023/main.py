from typing import * 

class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        
        def match(q, p): 
            m, n = len(q), len(p)
            i, j = 0, 0 
            while i < m and j < n: 
                if q[i] == p[j]: 
                    i += 1 
                    j += 1 
                elif q[i].islower(): 
                    i += 1 
                else: 
                    return False 
            while i < m: 
                if q[i].isupper():
                    return False 
                i += 1 
            return j == n 
        
        n = len(queries)
        ans = [0]*n 
        for i, q in enumerate(queries): 
            ans[i] = match(q, pattern)
            
        return ans 
    
if __name__ == "__main__": 
    s = Solution() 
    
    queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]
    pattern = "FB"
    assert s.camelMatch(queries, pattern) == [True,False,True,True,False]