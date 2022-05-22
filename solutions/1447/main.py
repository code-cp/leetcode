from typing import List 

def computeGCD(x, y):
   while(y):
       x, y = y, x % y
   return x

class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        result = []
        for denom in range(2, n+1): 
            for num in range(1, denom):
                if computeGCD(num, denom) == 1: 
                    result.append(f"{num}/{denom}")
        return result  

if __name__ == "__main__": 
    s = Solution()
    assert s.simplifiedFractions(2) == ["1/2"]