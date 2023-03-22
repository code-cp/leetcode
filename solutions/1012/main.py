class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        def perm(m, n): 
            # choose m numbers from n 
            res = 1 
            for i in range(n): 
                res *= (m-i)
            return res 
        
        n_str = str(n)
        n_len = len(n_str)
        res = 0 
        for i in range(1, n_len):
            res += perm(10, i) - perm(9, i-1)
        visited = [0]*10 
                
        def dfs(s, i):
            # use nonlocal instead of global https://stackoverflow.com/a/70502721/8519188
            nonlocal res 
            nonlocal visited 
            n = len(s)
            if i >= n: 
                res += 1 
                return 
            for d in range(10): 
                if i == 0 and d == 0: 
                    continue  
                if visited[d] == 1: 
                    continue 
                if d < int(s[i]): 
                    res += perm(10-(i+1), n-1-i)
                elif d == int(s[i]):
                    visited[d] = 1   
                    dfs(s, i+1)
                    visited[d] = 0 
        
        dfs(n_str, 0)
        return n-res     
        
if __name__ == "__main__": 
    s = Solution() 
    
    assert s.numDupDigitsAtMostN(20) == 1 