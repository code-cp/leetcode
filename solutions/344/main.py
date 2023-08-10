from typing import * 

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        You must do this by modifying the input array in-place with O(1) extra memory.
        """
        i, j = 0, len(s)-1
        while i < j: 
            s[i], s[j] = s[j], s[i]
            i += 1 
            j -= 1 
        
        
        