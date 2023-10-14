class Solution:
    def splitNum(self, num: int) -> int:
        digits = []
        while num > 0: 
            d = num % 10 
            digits.append(str(d))
            num //= 10 
            
        digits.sort()
        # assign the digits alternatively 
        num1 = "".join(digits[::2])
        num2 = "".join(digits[1:][::2])
        
        return int(num1) + int(num2)