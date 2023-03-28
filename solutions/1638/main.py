# ref https://leetcode.cn/problems/count-substrings-that-differ-by-one-character/solutions/2192088/tong-ji-zhi-chai-yi-ge-zi-fu-de-zi-chuan-z8xi/

class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dpl = [[0]*(n+1) for _ in range(m+1)]
        dpr = [[0]*(n+1) for _ in range(m+1)]
        res = 0 
        # for dpl, starts with index 1, index range is [1,n]
        # init is dpl[0]
        for i in range(m): 
            for j in range(n):
                if s[i] == t[j]:
                    dpl[i+1][j+1] = dpl[i][j]+1 
        # for dpr, starts with index 0, index range is [0,n-1]
        # init is dpr[n]
        for i in range(m-1, -1, -1): 
            for j in range(n-1, -1, -1):
                if s[i] == t[j]:
                    dpr[i][j] = dpr[i+1][j+1]+1 
        for i in range(m): 
            for j in range(n): 
                if s[i] != t[j]:
                    # NOTE, dpl[i][j] not dpl[i+1][j+1]
                    res += (dpl[i][j]+1)*(dpr[i+1][j+1]+1)
        return res 