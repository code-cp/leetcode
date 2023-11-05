from typing import * 

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        L = 10 
        idx = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        
        n = len(s)
        if n < L: 
            return []
        
        # total 8 x 4 = 32 bits 
        mask = 0x000FFFFF
        state = 0 
        ans = []
        memo = {}
        
        update_state = lambda state, ch: ((state << 2) | idx[ch]) & mask 
        
        # NOTE, L-1, not L!!!
        # only put the first 9 characters into state 
        for i in range(L-1): 
            state = update_state(state, s[i]) 
        
        for i in range(n-L+1): 
            state = update_state(state, s[i+L-1]) 
            memo[state] = memo.get(state, 0) + 1
            if memo[state] == 2: 
                # NOTE, do not add the same substr
                # only add when count == 2 
                ans.append(s[i:i+L])
              
        return ans 

if __name__ == "__main__": 
    s = Solution()
    
    assert s.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT") == ["AAAAACCCCC","CCCCCAAAAA"]
        
        
        