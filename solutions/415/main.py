class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        def str2num(s): 
            num = 0 
            n = len(s)
            for i in range(n): 
                num += (10**i) * (ord(s[n-i-1]) - ord('0')) 
            return num 
    
        n1 = str2num(num1)
        n2 = str2num(num2)
        total = n1 + n2 
        
        # ValueError: Exceeds the limit (4300) for integer string conversion; 
        # return str(ans)

        ans = ""
        if total == 0: 
            return "0"
        
        while total > 0: 
            ans += chr(total % 10 + ord("0")) 
            total //= 10 
        
        return ans[::-1]

if __name__ == "__main__": 
    s = Solution()
    
    assert s.addStrings("11", "123") == "134"
