class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        res = []
        # format is aa..a???
        # ??? can be as large as possible 
        for i in range(n-1, -1, -1): 
            # n <= k <= 26 * n
            # so k always >= i 
            idx = min(k-i, 26)
            res.append(chr(idx+ord("a")-1))
            k -= idx 
        res = "".join(res[::-1])
        return res 

if __name__ == "__main__": 
    s = Solution() 

    assert s.getSmallestString(3, 27) == "aay"