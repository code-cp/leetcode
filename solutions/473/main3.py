from typing import * 

class Solution: 
    def makesquare(self, matchsticks: List[int]) -> bool:
        self.success = False 
        total = sum(matchsticks) 
        matchsticks = sorted(matchsticks, reverse=True) 

        if total % 4 != 0:
            return False
        target = total // 4 

        def dfs(target, matchsticks, i, a, b, c, d): 
            sides = [a, b, c, d]
            # base case 
            if self.success: 
                return 
            eq_sides = len(set(sides)) == 1
            if i == len(matchsticks):
                if eq_sides and sides[0] == target:
                    self.success = True 
                return 
            # for duplicated values 
            if eq_sides and len(set(matchsticks[i:])) == 1 and len(matchsticks[i:]) % 4 == 0: 
                self.success = True 
                return 

            if a + matchsticks[i] <= target:
                dfs(target, matchsticks, i+1, a + matchsticks[i], b, c, d)
            if b + matchsticks[i] <= target:
                dfs(target, matchsticks, i+1, a, b + matchsticks[i], c, d)
            if c + matchsticks[i] <= target:
                dfs(target, matchsticks, i+1, a, b, c + matchsticks[i], d)
            if d + matchsticks[i] <= target:
                dfs(target, matchsticks, i+1, a, b, c, d + matchsticks[i])

        dfs(target, matchsticks, 0, 0, 0, 0, 0) 
        return self.success 

if __name__ == "__main__": 
    s = Solution() 

    matchsticks = [1,1,2,2,2]
    assert s.makesquare(matchsticks) 

    matchsticks = [3,3,3,3,4]
    assert not s.makesquare(matchsticks) 

    matchsticks = [2,2,2,2,2,2]
    assert not s.makesquare(matchsticks) 

    matchsticks = [20,13,19,19,4,15,10,5,5,15,14,11,3,20,11]
    assert s.makesquare(matchsticks) 

    matchsticks = [3,1,3,3,10,7,10,3,6,9,10,3,7,6,7]
    assert s.makesquare(matchsticks)

    matchsticks = [2,2,2,3,4,4,4,5,6]
    assert s.makesquare(matchsticks)

    matchsticks = [3,3,2,2,2,2,2,2,2,2,2,2,2,2,2]
    assert s.makesquare(matchsticks)

    matchsticks = [2,9,4,10,9,3,10,3,6,2,2,9,4,3,8]
    assert s.makesquare(matchsticks)

    matchsticks = [5969561,8742425,2513572,3352059,9084275,2194427,1017540,2324577,6810719,8936380,7868365,2755770,9954463,9912280,4713511]
    assert not s.makesquare(matchsticks)

