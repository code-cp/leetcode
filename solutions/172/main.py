class Solution:
    def trailingZeroes(self, n: int) -> int:
        result = 0 
        while n > 0: 
            result += n // 5
            n //= 5 
        return result  

if __name__ == "__main__": 
    s = Solution()

    n = 5
    assert s.trailingZeroes(n) == 1