from typing import * 

class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        n = len(price)
        def calNum(d): 
            res = 1
            cur = price[-1]
            for i in range(n-2, -1, -1): 
                if cur - price[i] >= d:
                    res +=1 
                    cur = price[i]
            return res  

        l, r = 0, max(price)-min(price)
        while l <= r: 
            mid = (r-l)//2+l 
            if calNum(mid) >= k: 
                l = mid+1 
            else: 
                r = mid-1 
        return l-1

if __name__ == "__main__": 
    s = Solution() 

    price = [13,5,1,8,21,2]
    k = 3
    assert s.maximumTastiness(price, k) == 8 