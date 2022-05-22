class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        # check whether n has alternating bits, 101010... or 010101... 
        # eg 5 = 101 
        # 5 >> 1 = 10 
        # 101 ^ 10 = 111 
        # 111 & 1000 = 0 
        temp = n ^ (n >> 1) 
        return temp & (temp + 1) == 0 

if __name__ == "__main__": 
    s = Solution()
    assert s.hasAlternatingBits(5)
    assert not s.hasAlternatingBits(7)
