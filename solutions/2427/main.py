class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        def gcd(a, b):
            if b == 0: 
                return a 
            return gcd(b, a%b)

        g = gcd(a, b)
        res = 1 
        for i in range(1, g): 
            if a%i == 0 and b%i == 0:
                res += 1 
        return res 