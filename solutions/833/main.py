from typing import * 

class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        sorted_indices = sorted(range(len(indices)), key=lambda i: indices[i])
        
        ans = ""
        m = 0
        i = 0 
        while i < len(s):
            if m == len(sorted_indices):
                ans += s[i]
                i += 1 
                continue 
            idx = sorted_indices[m]
            if i != indices[idx]:
                ans += s[i]
                i += 1 
                continue 
            j = i 
            k = 0
            while k < len(sources[idx]) and j < len(s) and s[j] == sources[idx][k]:
                j += 1 
                k += 1 
            if k == len(sources[idx]):
                ans += targets[idx]
                i += k 
            m += 1 
            
        return ans 

if __name__ == "__main__":
    s = Solution()
    
    assert s.findReplaceString("abcd", [0, 2], ["a", "cd"], ["eee", "ffff"]) == "eeebffff"