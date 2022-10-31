class Solution:
    def magicalString(self, n: int) -> int:
        res = 1 
        if n <= 3: 
            return res 
        # s = "1221121221221121122……"
        upper = "122"
        cur_idx = 3 
        # "1 2 2 1 1 2 1 2 2 1 2 2 ......"
        lower = "122"
        cnt_idx = 3
        while cur_idx < n: 
            # update res 
            if int(upper[-1])^3 == 1: 
                res += int(lower[-1])
                if cur_idx + int(lower[-1]) >= n:
                    res -= cur_idx + int(lower[-1]) - n 
            # update upper 
            upper += str(int(upper[-1])^3) * int(lower[-1])
            cur_idx += int(lower[-1])
            # update lower 
            lower += upper[cnt_idx]
            cnt_idx += 1 
        return res 

if __name__ == "__main__": 
    s = Solution() 

    assert s.magicalString(4) == 2 
    assert s.magicalString(6) == 3 
