# time 36 ms 
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        # dp table 
        prev, curr = 0, 0  
        # initialize 
        prev = 1
        if n == 0: 
            return prev
        curr = 10 
        # traverse 
        for i in range(2, n+1): 
            temp = curr 
            curr = curr + (curr - prev) * (10 - (i-1))
            prev = temp 
        return curr

if __name__ == "__main__": 
    s = Solution() 

    n = 2 
    result = s.countNumbersWithUniqueDigits(n) 
    assert result == 91 