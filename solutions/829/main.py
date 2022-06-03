from typing import * 

# sum = x + x+1 + ... + x+w-1 = N
# (x + x+w-1) * w / 2 = N 
# fix w, x = N/w - w/2 + 1/2 
# x = (2N - w^2 + w)/2w
import math 
class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        res = 0 
        for i in range(1, int(math.sqrt(2*n))+1):
            if (2*n - i*i + i) % (2*i) == 0:
                res += 1
        return res 

if __name__ == "__main__": 
    s = Solution() 

    assert s.consecutiveNumbersSum(5) == 2 