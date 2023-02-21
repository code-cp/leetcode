class Solution:
    def minOperations(self, n: int) -> int:
        if n == 0: 
            return 0 
        if n == 1: 
            return 1 

        p = 0 
        while 2**p < n: 
            p += 1 
        diff = min(abs(n-2**(max((p-1), 0))), abs(n-2**p))
        res = self.minOperations(diff) + 1 

        return res 

if __name__ == "__main__": 
    s = Solution() 

    assert s.minOperations(39) == 3 