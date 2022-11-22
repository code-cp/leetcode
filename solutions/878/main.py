class Solution: 
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        M = 1e9 + 7 

        def gcd(a, b): 
            while b: 
                a, b = b, a%b 
            return a 

        def getNum(num, a, b): 
            lcm = a*b/gcd(a, b)
            # NOTE, use // instead of / 
            res = num//a + num//b - num//lcm 
            return res 

        l, r = 1, n*max(a, b)
        while l <= r: 
            mid = (r-l)//2+l 
            num = getNum(mid, a, b)
            if num < n: 
                l = mid+1 
            else: 
                r = mid-1 

        return int(l%M)


if __name__ == "__main__": 
    s = Solution()

    assert s.nthMagicalNumber(3, 6, 4) == 8
    assert s.nthMagicalNumber(1, 2, 3) == 2 
        
