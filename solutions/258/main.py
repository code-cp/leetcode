class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            total = 0 
            while num >= 1:
                total += num % 10 
                num //= 10 
            num = total  
        return num 

if __name__ == "__main__": 
    s = Solution()

    # num = 38
    # assert s.addDigits(num) == 2 

    num = 10 
    assert s.addDigits(num) == 1