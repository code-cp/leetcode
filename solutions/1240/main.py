class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        if n > m: 
            n, m = m, n 
        # worset case 
        ans = n*m 
        # only record the heights 
        h = [0]*n 
        
        def dfs(cur): 
            nonlocal ans 
            
            # cur is no. of current squares used 
            # this is used for pruning 
            if cur >= ans: 
                return 
            
            mi = min(h)
            if mi == m: 
                ans = cur 
                return 
            
            mi_idx = h.index(mi)
            # find max. size 
            # (i-mi_idx+1+mi) <= m means the height can not exceed the max. height 
            i = mi_idx
            while i < n and h[i] == h[mi_idx] and ((i-mi_idx+1+mi) <= m): 
                i += 1
            for j in range(i-1, mi_idx-1, -1):
                # max. size of square 
                s = j-mi_idx+1
                # k only need to start from mi_idx
                # since it's the first place that has min value 
                for k in range(mi_idx, j+1): 
                    h[k] += s 
                # recurse 
                dfs(cur+1)
                # backtrack 
                for k in range(mi_idx, j+1): 
                    h[k] -= s  
            
        dfs(0)
        
        return ans 
                  
            
if __name__ == "__main__": 
    s = Solution() 
    
    # assert s.tilingRectangle(2, 3) == 3      
    # assert s.tilingRectangle(5, 8) == 5   
    assert s.tilingRectangle(11, 13) == 6