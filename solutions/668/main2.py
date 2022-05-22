from typing import * 

class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def count(x):
            total = 0 
            for i in range(1, n+1):
                total += min(x // i, m) 
            return total < k 

        start, end = 1, m*n 
        while start <= end: 
            mid = (end - start) // 2 + start 
            if count(mid): 
                start = mid + 1 
            else: 
                end = mid - 1
        return start 

if __name__ == "__main__": 
    s = Solution() 

    m = 3
    n = 3
    k = 5
    assert s.findKthNumber(m, n, k) == 3 

    m = 2
    n = 3
    k = 6
    assert s.findKthNumber(m, n, k) == 6 

    m = 9895
    n = 28405
    k = 100787757
    assert s.findKthNumber(m, n, k) == 31666344