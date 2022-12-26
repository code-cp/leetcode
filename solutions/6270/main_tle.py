# TLE 

from collections import Counter 
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0: 
            return 0 

        def check(ms): 
            cnt = Counter(ms)
            for key in ["a", "b", "c"]: 
                if cnt[key] < k: 
                    return False 
            return True 
        
        if not check(s):
            return -1 

        n = len(s)
        s = s + s 
        res = float("inf")

        for i in range(0, n): 
            j = i+1
            while j < 2*n and not check(s[i:j+1]):
                j += 1 
            if i > 0 and j < n-1: 
                continue 
            res = min(res, j-i+1)

        return res 


if __name__ == "__main__": 
    sol = Solution() 

    s = "cbbac"
    k = 1 
    assert sol.takeCharacters(s, k) == 3 

    # s = "ccbabcc"
    # k = 1 
    # assert sol.takeCharacters(s, k) == 4 

    # s = "a"
    # k = 0
    # assert sol.takeCharacters(s, k) == 0 

    # s = "aabaaaacaabc"
    # k = 2
    # assert sol.takeCharacters(s, k) == 8 

    # s = "a"
    # k = 1
    # assert sol.takeCharacters(s, k) == -1 