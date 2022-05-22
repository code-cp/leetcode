# TLE 
import heapq 
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
        pq = []
        for i in range(10**n-1, 10**(n-1)-1, -1): 
            heapq.heappush(pq, (-(i * (10**n-1)), i, 10**n-1))
        while True: 
            res_neg, i, j = heapq.heappop(pq)
            if self.isPalNum(-res_neg):
                return -res_neg % 1337 
            heapq.heappush(pq, (-(i * (j-1)), i, j-1))

if __name__ == "__main__": 
    s = Solution()

    n = 2 
    result = s.largestPalindrome(n)
    assert result ==  9009 % 1337

    n = 1
    result = s.largestPalindrome(n)
    assert result ==  9 % 1337