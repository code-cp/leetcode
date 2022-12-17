class Solution:
    def getLucky(self, s: str, k: int) -> int:
        def getSum(num): 
            res = 0 
            while num > 0: 
                res += num % 10 
                num //= 10 
            return res 

        res = 0 
        for ch in s: 
            res += getSum(ord(ch)-ord("a")+1)

        if k == 1: 
            return res 
        
        k -= 1 
        while k > 0: 
            res = getSum(res)
            k -= 1 

        return res 

if __name__ == "__main__": 
    sol = Solution() 
    
    s = "iiii"
    k = 1
    assert sol.getLucky(s, k) == 36 