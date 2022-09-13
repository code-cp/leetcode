class Solution:
    def maximumSwap(self, num: int) -> int:
        def num2digits(num): 
            digits = []
            while num > 0: 
                n = num%10 
                digits.append(n)
                num //= 10 
            return digits[::-1]

        def lastInd(digits, val): 
            for i in range(len(digits)-1, -1, -1): 
                if digits[i] == val: 
                    return i 

        digits = num2digits(num)
        original = [d for d in digits]
        digits.sort(reverse=True)
        for i in range(len(digits)): 
            if original[i] != digits[i]: 
                j = lastInd(original, digits[i])
                original[i], original[j] = original[j], original[i]
                break 
        res = 0 
        for d in original: 
            res += d 
            res *= 10
        res //= 10
        return res 

if __name__ == "__main__": 
    s = Solution()

    num = 98368
    assert s.maximumSwap(num) == 98863

    num = 2736
    assert s.maximumSwap(num) == 7236
