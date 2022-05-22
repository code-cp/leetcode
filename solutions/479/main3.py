class Solution:
    def isPalNum(self, num):
        return str(num) == str(num)[::-1] 
    def largestPalindrome(self, n: int) -> int:
        if n == 1: 
            return 9 
        upper = 10 ** n - 1 
        for left in range(upper, upper // 10, -1): 
            p, x = left, left 
            while x: 
                p = p * 10 + x % 10 
                x //= 10 
            x = upper 
            while x * x >= p: 
                if p % x == 0: 
                    return p % 1337 
                x -= 1 

if __name__ == "__main__": 
    s = Solution()

    n = 2 
    result = s.largestPalindrome(n)
    assert result ==  9009 % 1337

    # n = 1
    # result = s.largestPalindrome(n)
    # assert result ==  9 % 1337

    n = 7
    result = s.largestPalindrome(n)
    assert result ==  877

    # n = 8
    # result = s.largestPalindrome(n)
    # assert result ==  475