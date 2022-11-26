from typing import * 

# TLE 
# s =
# "heeelllooo"
# words =
# ["hellllo"]

class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        s_chars = []
        i = 1
        cnt = 1  
        while i < len(s): 
            while i < len(s) and s[i-1] == s[i]: 
                cnt += 1
                i += 1 
            if cnt >= 3: 
                s_chars.append(i-1)
                cnt = 1 
            i += 1 
        
        res = 0 
        for w in words: 
            i = j = 0 
            cnt = 1 
            while i < len(s) and j < len(w): 
                if s[i] == w[j]: 
                    i += 1 
                    j += 1 
                elif j > 0:
                    while i < len(s) and j-1 < len(w) and s[i] == w[j-1]: 
                        i += 1 
                    if i-1 not in s_chars:
                        cnt = 0  
                        break 
                else: 
                    cnt = 0 
                    break 
            while i < len(s) and s[i] == w[-1]: 
                i += 1 
                if i == len(s): 
                    if i-1 not in s_chars: 
                        cnt = 0 
            if i != len(s) or j != len(w): 
                cnt = 0 
            res += cnt
        return res 

if __name__ == "__main__": 
    sol = Solution()

    s = "lee"
    words = ["le"]
    assert sol.expressiveWords(s, words) == 0

    s = "abcd"
    words = ["abc"]
    assert sol.expressiveWords(s, words) == 0

    s = "heeellooo"
    words = ["hello", "hi", "helo"]
    assert sol.expressiveWords(s, words) == 1 

            


