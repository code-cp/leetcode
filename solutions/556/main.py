class Solution:
    def nextGreaterElement(self, n: int) -> int:
        def getDigits(n): 
            digits = []
            while n > 0: 
                d = n % 10 
                digits.append(d)
                n //= 10 
            digits = digits[::-1]
            return digits

        def getN(digits): 
            res = 0
            for d in digits:
                res += d 
                res *= 10  
            res //= 10 
            return res 

        digits = getDigits(n)
        if len(digits) < 2: 
            return -1 
        
        j = 0 
        for i in range(len(digits)-2, -1, -1): 
            if digits[i] < digits[i+1]:
                j = i 
                break 
        swap = False 
        for i in range(len(digits)-1, j, -1):
            if digits[i] > digits[j]:
                digits[i], digits[j] = digits[j], digits[i]
                swap = True 
                break  
        if not swap: 
            i = len(digits)-1
            digits[i], digits[j] = digits[j], digits[i]
        digits[j+1:] = digits[j+1:][::-1]
        res = getN(digits)
        if res <= n: 
            return -1 
        if res > 2 ** 31 - 1: 
            return -1 

        return res 

if __name__ == "__main__": 
    s = Solution()

    assert s.nextGreaterElement(12) == 21 
    assert s.nextGreaterElement(21) == -1 
    assert s.nextGreaterElement(101) == 110 
    assert s.nextGreaterElement(230241) == 230412 
    assert s.nextGreaterElement(2147483476) == 2147483647 