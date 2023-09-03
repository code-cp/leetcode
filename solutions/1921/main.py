from typing import * 
import math 
class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        n = len(dist)
        steps = [math.ceil(dist[i]/speed[i]) for i in range(n)]
        steps.sort()
        
        ans = 0
        i = 0 
        time_from_start = 0 
        while i < n: 
            if i == 0: 
                ans += 1 
                i += 1 
                time_from_start += 1 
                continue
            # no time to reload 
            if steps[i] - time_from_start <= 0 and steps[i] - steps[i-1] <= 1:
                return ans
            
            time_from_start += 1  
            ans += 1
            i += 1  
        
        return ans 
    
if __name__ == '__main__': 
    s = Solution()
    
    assert s.eliminateMaximum([1,3,4],[1,1,1]) == 3 