from typing import List 

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        alphabets = [0] * 26
        for m in magazine:
            alphabets[ord(m)-ord('a')] += 1
        for r in ransomNote:
            alphabets[ord(r)-ord('a')] -= 1
            if alphabets[ord(r)-ord('a')] < 0:
                return False
        return True

if __name__ == "__main__": 
    ransomNote = "aa"
    magazine = "aab"
    s = Solution()
    assert s.canConstruct(ransomNote, magazine)
