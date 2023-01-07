class Solution:
    def countEven(self, num: int) -> int:
        def dSum(d):
            res = 0 
            while d > 0: 
                res += d%10 
                d //= 10 
            return res 

        res = 0 
        for i in range(1, num+1): 
            if dSum(i) % 2 == 0: 
                res += 1 
        
        return res 