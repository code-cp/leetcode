class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        prefix = [0]*n 
        suffix = [0]*n 
        
        num_b = 0 
        for i in range(n): 
            if s[i] == "b": 
                num_b += 1 
            prefix[i] = num_b
            
        num_a = 0 
        for i in range(n-1, -1, -1): 
            if s[i] == "a": 
                num_a += 1 
            suffix[i] = num_a
            
        # can only delete b on the left 
        # and only delete a on the right 
        res = float("inf")
        for i in range(n):
            # NOTE, cur position is deleted twice, need to -1
            res = min(res, prefix[i] + suffix[i] - 1) 
            
        return res  
            
if __name__ == "__main__": 
    sol = Solution() 
    
    assert sol.minimumDeletions("bbaaaaabb") == 2 