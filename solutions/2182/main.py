from typing import * 
from collections import Counter 

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        chars = Counter(s)
        unique_chars = sorted(list(set(s)), reverse=True)

        i = j = 0 
        ans = ""
        while i < len(unique_chars): 
            # process char i 
            while chars[unique_chars[i]] > 0:
                num = min(repeatLimit, chars[unique_chars[i]])
                ans += unique_chars[i] * num
                chars[unique_chars[i]] -= num  
                if chars[unique_chars[i]] > 0:
                    # find the next char 
                    if j <= i:
                        j = i + 1 
                    while j < len(unique_chars) and chars[unique_chars[j]] == 0:
                        j += 1 
                    if j < len(unique_chars):
                        ans += unique_chars[j] 
                        chars[unique_chars[j]] -= 1
                    else: 
                        return ans 
            i += 1 
        return ans 
        
if __name__ == "__main__": 
    s = Solution()
    # assert s.repeatLimitedString("cczazcc", 3) == "zzcccac"
    # assert s.repeatLimitedString("robnsdvpuxbapuqgopqvxdrchivlifeepy", 2) == "yxxvvuvusrrqqppopponliihgfeeddcbba"
    assert s.repeatLimitedString("xyutfpopdynbadwtvmxiemmusevduloxwvpkjioizvanetecnuqbqqdtrwrkgt", 1) == "zyxyxwxwvwvuvuvututstrtrtqpqpqponononmlmkmkjigifiededededcbaba"
                