from typing import * 

class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        n = len(s)
        ans = [False]*len(queries)
        prefix = [[0]*26 for _ in range(n+1)]
        
        for i in range(n):
            for j in range(26): 
                prefix[i+1][j] = prefix[i][j]
            idx = ord(s[i]) - ord("a")
            prefix[i+1][idx] = prefix[i][idx] + 1 
            
        for i, q in enumerate(queries): 
            cur = s[q[0]:q[1]+1]
            k = q[2]
            pre = [0]*26 
            cnt_odd = 0 
            for j in range(26):
                pre[j] = prefix[q[1]+1][j] - prefix[q[0]][j]
                if pre[j] % 2 == 1: 
                    cnt_odd += 1 
            if (cnt_odd - 1) / 2 <= k: 
                ans[i] = True 
                
        return ans 
            
if __name__ == "__main__": 
    s = Solution() 

    st = "abcda"
    queries = [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]
    assert s.canMakePaliQueries(st, queries) == [True,False,False,True,True]
    
    # st = "lyb"
    # queries = [[0,1,0],[2,2,1]]
    # assert s.canMakePaliQueries(st, queries) == [False, True]