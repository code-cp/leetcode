from typing import * 

class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        n = len(slices)
        
        # never pick adjacent slices 
        # end -> start wrap 
        # pick n slices 
        def solve(start, end, k): 
            nonlocal slices 
            nonlocal n 
            
            dp = [[[0]*(k+1) for _ in range(n+1)] for _ in range(2)]
        
            for i in range(start, end+1):
                # all slices avaliable are i-start+1
                for j in range(1, min(k, i-start+1)+1): 
                    # max. gain when we do not pick i-th slice 
                    # with total j slices so far 
                    # we can pick i-1 slice 
                    dp[0][i][j] = max(dp[0][i-1][j], dp[1][i-1][j]) 
                    # max. gain when we pick i-th slice 
                    # with total j slices so far 
                    # then we cannot pick i-1 slice 
                    dp[1][i][j] = dp[0][i-1][j-1] + slices[i-1]
            
            # NOTE, use end not n
            # dp[0][i] means pick from [1,i] slice 
            return max(dp[0][end][k], dp[1][end][k]) 
        
        # either choose the head or tail, but not both
        # NOTE, index starts with 1  
        res = max(solve(1, n-1, n//3), solve(2, n, n//3))
        return res 

if __name__ == '__main__': 
    s = Solution()
    
    # assert s.maxSizeSlices([1,2,3,4,5,6]) == 10
    assert s.maxSizeSlices([8,9,8,6,1,1]) == 16