from typing import * 

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0 
        while i < len(bits): 
            if i == len(bits)-1: 
                return True 
            if bits[i] == 1: 
                i += 2
            elif bits[i] == 0: 
                i += 1 
        return False 

if __name__ == "__main__": 
    s = Solution()
    bits = [1, 0, 0]
    assert s.isOneBitCharacter(bits) 
    bits = [1, 1, 1, 0]
    assert not s.isOneBitCharacter(bits)