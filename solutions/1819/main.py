from typing import * 

import math 
class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        def gcd(a, b): 
            while b > 0: 
                a, b = b, a%b 
            return a 

        g = [0]*(2*(10**5)+1)
        for n in nums: 
            for i in range(1, int(math.sqrt(n))+1):
                if n % i == 0: 
                    if g[i] == 0:
                        g[i] = n
                    else: 
                        g[i] = gcd(g[i], n)
                    if n//i != i:  
                        if g[n//i] == 0:
                            g[n//i] = n
                        else: 
                            g[n//i] = gcd(g[n//i], n)

        # number of different GCDs among all non-empty subsequences of nums
        count = 0 
        for i in range(1, 2*(10**5)+1): 
            if i == g[i]: 
                count += 1 

        return count 

if __name__ == "__main__": 
    s = Solution() 
    
    nums = [6,10,3]
    assert s.countDifferentSubsequenceGCDs(nums) == 5 