class Solution:
    def pivotInteger(self, n: int) -> int:
        if n == 1: 
            return 1 

        def checkValid(x, n): 
            return (1+x)*x/2 == (x+n)*(n-x+1)/2
                
        for x in range(n//2,n): 
            if checkValid(x,n):
                return x 
            
        return -1 