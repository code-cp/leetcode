class Solution:
    def queryString(self, s: str, n: int) -> bool:        
        # We only need to check substrings of length at most 30, because 10^9 has 30 bits.
        def int2str(num): 
            ans = ""
            while num > 0: 
                ans += str(num % 2) 
                num //= 2 
            return ans[::-1]
        
        for i in range(1, n+1):
            sn = int2str(i)
            if sn not in s: 
                return False 
            
        return True  
            
        