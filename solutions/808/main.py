from functools import lru_cache

class Solution:
    def soupServings(self, n: int) -> float:
        if n > 5000: 
            return 1.0 

        # NOTE, need to set the maxsize large 
        @lru_cache(maxsize=1000)
        def dfs(a, b): 
            # base case 
            if a == 0 and b != 0: 
                return 1.0 
            if a == 0 and b == 0: 
                return 0.5 
            if a != 0 and b == 0: 
                return 0 

            subtract = lambda x, y: x-min(x, y)

            prob = 0 
            prob += 0.25 * dfs(subtract(a, 100), b)
            prob += 0.25 * dfs(subtract(a, 75), subtract(b, 25))
            prob += 0.25 * dfs(subtract(a, 50), subtract(b, 50))
            prob += 0.25 * dfs(subtract(a, 25), subtract(b, 75))

            return prob 

        return dfs(n, n)

if __name__ == "__main__": 
    s = Solution() 

    assert s.soupServings(50) == 0.62500 
    assert s.soupServings(100) == 0.71875