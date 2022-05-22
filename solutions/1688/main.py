class Solution:
    def numberOfMatches(self, n: int) -> int:
        result = 0
        while n > 1: 
            if n % 2 == 1: 
                result += (n-1) / 2 
                n = (n-1) / 2 + 1
            else: 
                result += n / 2 
                n = n / 2 
        return int(result) 

if __name__ == "__main__": 
    n = 7 
    s = Solution()
    assert s.numberOfMatches(n) == 6
