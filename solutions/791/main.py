
from collections import Counter 
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        cnt = Counter(s)
        res = ""
        for ch in order: 
            res += ch * cnt[ch]
        for ch in s: 
            if ch not in order: 
                res += ch 
        return res 

if __name__ == "__main__": 
    sol = Solution() 

    order = "cba"
    s = "abcd"
    assert sol.customSortString(order, s) == "cbad"