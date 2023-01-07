class Solution:
    def repeatedCharacter(self, s: str) -> str:
        letters = {}
        for ch in s: 
            if letters.get(ch, 0) != 0: 
                return ch 
            else: 
                letters[ch] = 1 
        
