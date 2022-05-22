from typing import * 

# O(n)
# TLE 
# 9885387
# 8786251
# class Solution:
#     def traverse(self, start, n):
#         result = [] 
#         for i in range(10): 
#             j = start*10 + i 
#             if j > n: 
#                 return result 
#             # visit 
#             result += [j] 
#             # L, R 
#             result += self.traverse(j, n)
#         return result 
#     def findKthNumber(self, n: int, k: int) -> int:
#         result = []
#         k -= 1 
#         if n < 10: 
#             result = list(range(1, n+1))
#             return result[k]
#         for i in range(1, 10): 
#             # visit 
#             result += [i]
#             # L, R
#             result += self.traverse(i, n)
#         return result[k]

# O(k)
# TLE 
# 9885387
# 8786251
class Solution:
    def traverse(self, start, n):
        result = [] 
        for i in range(10): 
            j = start*10 + i  
            if j > n: 
                return result 
            # visit 
            if self.count > 0: 
                result += [j] 
            self.count -= 1
            if self.count <= 0:
                return result 
            # L, R 
            result += self.traverse(j, n)
        return result 
    def findKthNumber(self, n: int, k: int) -> int:
        result = []
        if n < 10: 
            result = list(range(1, n+1))
            return result[k-1]
        self.count = k
        for i in range(1, 10): 
            # visit 
            if self.count > 0: 
                result += [i]
            self.count -= 1 
            if self.count <= 0: 
                break 
            # L, R
            result += self.traverse(i, n)
        return result[-1]

if __name__ == "__main__": 
    s = Solution()

    n = 13
    k = 2
    assert s.findKthNumber(n, k) == 10

    # n = 13
    # k = 1
    # assert s.findKthNumber(n, k) == 1

    # n = 1
    # k = 1
    # assert s.findKthNumber(n, k) == 1

    # n = 2
    # k = 2
    # assert s.findKthNumber(n, k) == 2

    # n = 9885387
    # k = 8786251
    # assert s.findKthNumber(n, k) == 8907623

    # n = 10
    # k = 3
    # assert s.findKthNumber(n, k) == 2