from typing import * 

"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        res = []

        def bsearch(x, target): 
            l, r = 1, 1000
            while l <= r: 
                mid = (r-l)//2+l 
                val = customfunction.f(x, mid)
                if val > target: 
                    r = mid-1 
                elif val < target: 
                    l = mid+1 
                else: 
                    return mid
            return -1  

        for x in range(1, 1001): 
            y = bsearch(x, z)
            if y != -1:
                res.append([x, y]) 

        return res 
