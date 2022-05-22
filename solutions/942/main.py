from typing import * 

class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        res = []
        i, j = 0, n 
        for c in s: 
            if c == 'I': 
                res.append(i) 
                i += 1 
            else: 
                res.append(j)
                j -= 1 
        res.append(i)
        return res 

if __name__ == "__main__": 
    sol = Solution() 

    s = "IDID"
    print(sol.diStringMatch(s)) 