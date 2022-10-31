class Solution:
    def magicalString(self, n: int) -> int:
        if n <= 3: 
            return 1

        # s = "1221121221221121122……"
        upper = "122"
        cur_idx = 3 
        # "1 2 2 1 1 2 1 2 2 1 2 2 ......"
        lower = "122"
        cnt_idx = 3
        while cur_idx < n: 
            upper += str(int(upper[-1])^3) * int(lower[-1])
            cur_idx += int(lower[cnt_idx-1])
            
            lower += upper[cnt_idx]
            cnt_idx += 1 

        return upper[:n].count("1") 

if __name__ == "__main__": 
    s = Solution() 

    # assert s.magicalString(4) == 2 
    assert s.magicalString(6) == 3 
