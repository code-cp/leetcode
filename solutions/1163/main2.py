class Solution:
    def lastSubstring(self, s: str) -> str:
        n = len(s)
        max_char = max(s)
        
        candidates = [i for i, c in enumerate(s) if c == max_char]
        
        offset = 1 
        while len(candidates) > 1: 
            cur_max = max(s[i+offset] for i in candidates if i+offset < n)
            new_cand = []
            for i, st in enumerate(candidates):
                if i > 0 and candidates[i-1]+offset == st: 
                    continue 
                if st+offset < n and s[st+offset] == cur_max: 
                    new_cand.append(st)
                    
            candidates = new_cand 
            offset += 1 
        
        return s[candidates[0]:]