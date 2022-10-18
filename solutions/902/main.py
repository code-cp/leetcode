from typing import * 

# class Solution:
#     def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
#         n_str = str(n)
#         k = len(n_str)

#         res = 0 
#         for i in range(1, k):  
#             res += len(digits) ** i 

#         def dfs(cur, pos, res): 
#             # base case 
#             if pos == k: 
#                 res += 1 
#                 return res

#             for d in digits: 
#                 if d < n_str[pos]: 
#                     res += len(digits) ** (k-1-pos)
#                 elif d == n_str[pos]:
#                     res = dfs(cur*10 + int(d), pos+1, res)

#             return res 

#         res = dfs(0, 0, res)
#         return res 

class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        n_str = str(n)
        k = len(n_str)

        # NOTE, need to use global 
        global res  
        res = 0 
        for i in range(1, k):  
            res += len(digits) ** i 

        def dfs(cur, pos):
            global res  
            # base case 
            if pos == k: 
                res += 1 
                return 

            for d in digits: 
                if d < n_str[pos]: 
                    res += len(digits) ** (k-1-pos)
                elif d == n_str[pos]:
                    dfs(cur*10 + int(d), pos+1)

        dfs(0, 0)
        return res 
            
if __name__ == "__main__": 
    s = Solution()

    digits = ["7"]
    n = 8
    assert s.atMostNGivenDigitSet(digits, n) == 1

    digits = ["1","3","5","7"]
    n = 100
    assert s.atMostNGivenDigitSet(digits, n) == 20 

