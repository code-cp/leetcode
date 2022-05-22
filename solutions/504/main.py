class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0: 
            return "0"
            
        result = ""
        factor = 1 
        if num < 0: 
            factor = -1
            num *= -1 

        while num >= 1:
            result = str(num % 7) + result
            num //= 7
        if factor == -1: 
            result = "-" + result
        return result

if __name__ == "__main__": 
    s = Solution()

    num = 100
    assert s.convertToBase7(num) == "202"

    num = -7
    assert s.convertToBase7(num) == "-10"