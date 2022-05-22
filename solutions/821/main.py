from typing import * 

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        res = [0] * len(s) 
        char_pos = []
        for i, char in enumerate(s): 
            if char == c: 
                char_pos.append(i)
        for i, char in enumerate(s):
            if len(char_pos) >= 2 and abs(i - char_pos[0]) > abs(i - char_pos[1]):
                res[i] = abs(i-char_pos[1])
                char_pos.pop(0)
            else: 
                res[i] = abs(i-char_pos[0])
        return res 

if __name__ == "__main__": 
    s = Solution()
    
    result = s.shortestToChar("loveleetcode", 'e')
    assert result == [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]