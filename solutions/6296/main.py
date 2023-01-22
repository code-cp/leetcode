class Solution:
    def alternateDigitSum(self, n: int) -> int:
        digits = []
        while n > 0: 
            digits.append(n%10)
            n //= 10 
        res = 0
        pos = True  
        for i in range(len(digits)-1, -1, -1):
            if pos: 
                res += digits[i]
            else:
                res -= digits[i]
            pos = not pos 
        return res  

