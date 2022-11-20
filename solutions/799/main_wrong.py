from functools import lru_cache

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # calculate max level 
        # (n+1)*n/2 <= poured 
        M_LEV = 99 

        cal_total = lambda x: (x+1)*x/2

        def bsearch(target):
            l, r = 1, M_LEV+1
            while l <= r: 
                mid = (r-l)//2+l 
                if cal_total(mid) < target: 
                    l = mid+1 
                else: 
                    r = mid-1
            return l-1  

        # NOTE, level is 0-indexed 
        max_level = bsearch(poured)-1
        if max_level < 0: 
            return 0 
        if max_level >= query_row:
            return 1 
        if max_level+1 < query_row:
            return 0 

        res = poured - cal_total(max_level+1)
        per_cup = res / query_row

        if query_glass == 0 or query_glass == query_row:
            return per_cup / 2 
        
        return per_cup

if __name__ == "__main__": 
    s = Solution() 

    poured = 25
    query_row = 6
    query_glass = 1
    assert s.champagneTower(poured, query_row, query_glass) == 0.1875

    # poured = 0
    # query_row = 0
    # query_glass = 0
    # assert s.champagneTower(poured, query_row, query_glass) == 0

    # poured = 100000009
    # query_row = 33
    # query_glass = 17
    # assert s.champagneTower(poured, query_row, query_glass) == 1.00000

    # poured = 1
    # query_row = 1
    # query_glass = 1
    # assert s.champagneTower(poured, query_row, query_glass) == 0.00000

    # poured = 2
    # query_row = 1
    # query_glass = 1
    # assert s.champagneTower(poured, query_row, query_glass) == 0.50000
            