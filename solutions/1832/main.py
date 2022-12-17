class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        res = 0 
        for ch in sentence: 
            res |= (1<<(ord(ch)-ord("a")))
            if res == (1<<26)-1: 
                return True 
        return False 