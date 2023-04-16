class Solution:
    def longestDecomposition(self, text: str) -> int:
        
        def kmp(s: str) -> int:
            # -c--a*****----b
            n = len(s)
            dp = [0]*n 
            for i in range(1, n): 
                j = dp[i-1]
                while j > 0 and s[i] != s[j]: 
                    j = dp[j-1]
                if s[i] == s[j]: 
                    dp[i] = j+1 
            return dp[-1]
        
        ans = 0 
        s = text 
        l = kmp(s)
        while len(s) > 0 and l > 0: 
            n = len(s)
            c = 0 
            if 2*l > n: 
                l = n//2 
            i, j = 0, l-1 
            while i < j and s[i] == s[j]: 
                i += 1 
                j -= 1 
                c += 1 
            if c == 0: 
                # prefix cannot be divided 
                ans += 2    
            else: 
                # eg. anta 
                # x4 is because a##a 
                # x2 is because #nt# 
                ans += 4*c 
                if l != 2*c: 
                    ans += 2 
            s = s[l:n-l]
            if len(s) > 0:
                l = kmp(s)
        if len(s) > 0: 
            ans += 1 
        return ans 

if __name__ == "__main__": 
    s = Solution() 
    
    assert s.longestDecomposition("antaprezatepzapreanta") == 11 
    # assert s.longestDecomposition("elvtoelvto") == 2   
    # assert s.longestDecomposition("ghiabcdefhelloadamhelloabcdefghi") == 7           