class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        num = 2*n-2
        ans = time % num + 1 
        if ans > n: 
            ans = n - (ans - n)
        return ans   
       
if __name__ == "__main__": 
    s = Solution()
    
    assert s.passThePillow(18,38) == 5 