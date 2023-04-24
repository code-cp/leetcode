class Solution:
    def lastSubstring(self, s: str) -> str:
        n = len(s)
        ans = 0 
        
        # i = start of answer 
        # j = start of str to be compared 
        # k = commen part of suf_i, suf_j 
        def dfs(i,j,k):
            nonlocal n  
            nonlocal ans 
            # base case 
            if j+k >= n:
                ans = i 
                return
              
            if i+k == j:
                # eg cacacb, j can move directly to last c  
                dfs(i,j+k,0)
            elif s[i+k] == s[j+k]:
                # same -> compare next  
                dfs(i,j,k+1)
            elif s[i+k] > s[j+k]:
                # suf_i > suf_j -> i no change, j=j+k+1 
                # if k=0, j=j+1
                # if k>0, if j can be inside [j+1,j+k], then we already triggered last case 
                # suppose s[p]>s[i], p in [j+1,j+k]
                # then there must be s[q]>=s[p]>s[i], q in [i+1,i+k] 
                dfs(i,j+k+1,0)
            else: 
                # suf_i < suf_j -> i=j, j=j+1
                # i move to j since j may be the new answer 
                dfs(j,j+1,0)
                
        dfs(0,1,0)
        
        return s[ans:]

if __name__ == "__main__": 
    s = Solution() 
    
    # assert s.lastSubstring("abab") == "bab"
    # assert s.lastSubstring("leetcode") == "tcode"
    assert s.lastSubstring("cacacb") == "cb"