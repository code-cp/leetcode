# TLE 
from collections import Counter 
class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)
        res = 0 
        for i in range(n): 
            for j in range(i+1, n): 
                max_f = -1 
                min_f = float("inf")
                cnt = Counter(s[i:j+1])
                for ch in cnt.keys():
                    freq = cnt[ch]
                    max_f = max(max_f, freq)
                    min_f = min(min_f, freq)
                res += max_f - min_f 
        return res 

if __name__ == "__main__": 
    sol = Solution() 

    s = "aabcbaa"
    assert sol.beautySum(s) == 17 

    s = "aabcb"
    assert sol.beautySum(s) == 5 
