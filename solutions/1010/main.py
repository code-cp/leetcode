from typing import * 

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        ans = 0
        mod = [0]*60 
        for t in time: 
            m = t%60 
            ans += mod[(60-m)%60]
            mod[m] += 1 
        return ans 
    
if __name__ == "__main__": 
    s = Solution() 
    time = [30,20,150,100,40]
    assert s.numPairsDivisibleBy60(time) == 3 
            