class Solution:
    def numberOfCuts(self, n: int) -> int:
        if n == 1: 
            return 0 
        # NOTE, into n **equal** slices.
        if n % 2 == 0: 
            # n/2 - 1 + 1 = n/2 
            ans = n//2 
        else: 
            ans = n 
        return int(ans) 

             
            