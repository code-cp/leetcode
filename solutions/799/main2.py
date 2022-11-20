from functools import lru_cache

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0] * (query_glass+1) for _ in range(2)]
        dp[0][0] = poured 
        for l in range(1, query_row+1): 
            for g in range(query_glass+1): 
                if g == 0 or g == l: 
                    dp[1][g] = max(0, (dp[0][max(0, g-1)]-1)/2)
                else: 
                    dp[1][g] = max(0, (dp[0][g-1]-1)/2) + max(0, (dp[0][g]-1)/2)
            dp[0] = [x for x in dp[1]]
        res = min(1, dp[0][-1])
        return res

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
            