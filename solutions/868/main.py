class Solution:
    def binaryGap(self, n: int) -> int:
        res = 0 
        pre_pos, cur_pos = -1, 0
        while n > 0: 
            bit = n & 1 
            n >>= 1 
            if bit == 1: 
                if pre_pos >= 0: 
                    res = max(res, cur_pos - pre_pos) 
                pre_pos = cur_pos 
            cur_pos += 1 
        return res 

if __name__ == "__main__": 
    s = Solution() 

    result = s.binaryGap(22)
    assert result == 2 