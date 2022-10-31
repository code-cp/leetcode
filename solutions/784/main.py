from typing import * 

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        n = len(s)

        def dfs(idx, cur): 
            # base case 
            if idx == n:
                res.append(cur)
                return 
            
            if s[idx].lower().isalpha():
                dfs(idx+1, cur + s[idx].lower())
                dfs(idx+1, cur + s[idx].upper())
            else: 
                dfs(idx+1, cur + s[idx])
                
        dfs(0, "")

        return res 

if __name__ == "__main__": 
    sol = Solution() 

    s = "3z4"
    assert sol.letterCasePermutation(s) == ["3z4","3Z4"]