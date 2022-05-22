# TLE at n = 4 
class Solution:
    def isPalNum(self, num):
        num = [int(x) for x in str(num)]
        i, j = 0, len(num) - 1 
        while i < j: 
            if num[i] != num[j]: 
                return False 
            i += 1 
            j -= 1
        return True 
    def largestPalindrome(self, n: int) -> int:
        max_res = 0 
        for i in range(10**n - 1, 10**(n-1)-1, -1): 
            for j in range(10**n - 1, 10**(n-1)-1, -1): 
                res = i * j 
                if self.isPalNum(res):
                    max_res = max(res, max_res) 
        return max_res % 1337 

if __name__ == "__main__": 
    s = Solution()

    n = 2 
    result = s.largestPalindrome(n)
    assert result ==  9009 % 1337

    n = 1
    result = s.largestPalindrome(n)
    assert result ==  9 % 1337