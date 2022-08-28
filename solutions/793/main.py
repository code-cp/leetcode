class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        def zero(x):
            res = 0 
            while x > 0: 
                x //= 5 
                res += x 
            return res 

        def bsearch(k):
            left, right = 0, 5*k 
            while left <= right: 
                mid = (right-left)//2+left 
                zero_num = zero(mid)
                if zero_num >= k: 
                    right = mid-1 
                else: 
                    left = mid+1 
            return left

        lower = bsearch(k)
        upper = bsearch(k+1)

        return upper-lower 

if __name__ == "__main__": 
    s = Solution()

    # assert s.preimageSizeFZF(0) == 5 
    assert s.preimageSizeFZF(5) == 0 
    # assert s.preimageSizeFZF(4) == 5 