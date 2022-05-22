class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0: 
            return 0 
        result = 1 
        if n < 0: 
            x, n = 1/x, -n 
        while n > 0: 
            if n & 1: 
                n -= 1 
                result *= x
            else: 
                n >>= 1 
                x *= x 
        return result 

if __name__ == "__main__": 
    s = Solution()
    x = 2.00000 
    n = 10
    assert s.myPow(x, n) == 1024.00000
    x = 2.00000
    n = -2
    assert s.myPow(x, n) == 0.25000