from collections import defaultdict

class Solution:
    def __init__(self): 
        self.max_len = 0
    def helper(self, s, k, count): 
        umap = defaultdict(int) 
        j = 0 
        valid = 0
        for i in range(len(s)): 
            while j < len(s) and len(umap) <= count: 
                umap[s[j]] += 1 
                if umap[s[j]] == k: 
                    valid += 1 
                if len(umap) == count and valid == count: 
                    self.max_len = max(self.max_len, j-i+1)
                j += 1 
            umap[s[i]] -= 1 
            if umap[s[i]] == k-1:
                valid -= 1 
            elif umap[s[i]] == 0: 
                del umap[s[i]]  
    def longestSubstring(self, s: str, k: int) -> int:
        for c in range(1, 26+1):
            self.helper(s, k, c)
        return self.max_len

if __name__ == "__main__": 
    s = "ababbc"
    k = 2 
    sol = Solution()
    assert sol.longestSubstring(s, k) == 5 