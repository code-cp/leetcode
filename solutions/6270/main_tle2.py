from collections import defaultdict
import math 
# TLE 

class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0: 
            return 0 
        n = len(s)

        pre_sum = [[0]*3 for _ in range(n)]
        for i in range(n): 
            idx = ord(s[i]) - ord("a")
            if i == 0: 
                pre_sum[i][idx] = 1 
            else: 
                for j in range(3): 
                    if j == idx: 
                        pre_sum[i][idx] = pre_sum[i-1][idx]+1
                    else: 
                        pre_sum[i][j] = pre_sum[i-1][j]

        suf_sum = [[0]*3 for _ in range(n)]
        for i in range(n-1, -1, -1): 
            idx = ord(s[i]) - ord("a")
            if i == n-1: 
                suf_sum[i][idx] = 1 
            else: 
                for j in range(3): 
                    if j == idx: 
                        suf_sum[i][idx] = suf_sum[i+1][idx]+1
                    else: 
                        suf_sum[i][j] = suf_sum[i+1][j]

        def check(arr): 
            for i in range(3): 
                if arr[i] < k: 
                    return False 
            return True 

        res1 = float("inf")
        for i in range(n): 
            if check(pre_sum[i]): 
                res1 = i+1 
                break 

        res2 = float("inf")
        for i in range(n-1, -1, -1): 
            if check(suf_sum[i]): 
                res2 = n-1-i+1  
                break 
        res = min(res1, res2)

        for i in range(1, n): 
            for j in range(0, i): 
                total = [0]*3
                for m in range(3): 
                    total[m] = suf_sum[i][m]+pre_sum[j][m]
                if check(total):
                    res = min(res, n-1-i+1+j+1)

        return res if math.isfinite(res) else -1 


if __name__ == "__main__": 
    sol = Solution() 

    s = "cbaabccac"
    k = 3
    assert sol.takeCharacters(s, k) == -1 

    # s = "cbbac"
    # k = 1 
    # assert sol.takeCharacters(s, k) == 3 

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