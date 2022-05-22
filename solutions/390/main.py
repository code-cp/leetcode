class Solution:
    def lastRemaining(self, n: int) -> int:
        step = 1 
        remain = n 
        head = 1 
        fromLeft = True 

        while remain > 1: 
            if fromLeft or remain % 2 == 1: 
                head += step 
            step *= 2 
            remain //= 2 
            fromLeft = not fromLeft

        return head  

if __name__ == "__main__": 
    n = 9
    s = Solution()
    assert s.lastRemaining(n) == 6
