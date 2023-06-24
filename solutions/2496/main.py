from typing import * 

class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        mx = 0 
        for w in strs:
            is_digit = True   
            for ch in w:
                if ch.islower(): 
                    mx = max(mx, len(w))
                    is_digit = False 
                    break 
            if is_digit: 
                mx = max(mx, int(w))
        return mx 
                 
                