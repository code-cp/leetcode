import math 

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1: 
            return False 
        total = 0 
        for i in range(1, math.floor(math.sqrt(num))+1): 
            if num % i == 0: 
                total += i 
                if i != 1 and i != math.sqrt(num): 
                    total += num / i 
            if total > num: 
                return False 
        return total == num 

if __name__ == "__main__": 
    s = Solution()
    num = 28 
    assert s.checkPerfectNumber(num)
    num = 7 
    assert not s.checkPerfectNumber(num)
