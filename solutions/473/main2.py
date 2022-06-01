from typing import * 

class Solution: 
    def dfs(self, target, remain, matchsticks, i, sides): 
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

        # greedy 
        idxs = sorted(range(len(sides)), key=sides.__getitem__, reverse=self.reverse_flag)
        for idx, j in enumerate(idxs):
            # prune 
            # if two sides have same len then skip since we already explored it 
            if idx != 0 and sides[idxs[idx]] == sides[idxs[idx-1]]: 
                continue 
            # if cannot reach target then skip 
            if sides[j] + remain < target: 
                return 
            if target - sides[j] != 0 and target - sides[j] < min(matchsticks[i:]):
                return 
            # if already exceeds target then skip 
            if sides[j] > target: 
                return 
            if sides[j] + matchsticks[i] > target: 
                continue 
            remain -= matchsticks[i] 
            sides[j] += matchsticks[i]
            self.dfs(target, remain, matchsticks, i+1, sides)
            sides[j] -= matchsticks[i]
            remain += matchsticks[i] 
        
    def makesquare(self, matchsticks: List[int]) -> bool:
        self.success = False 
        total = sum(matchsticks) 
        matchsticks = sorted(matchsticks, reverse=True) 

        if total % 4 != 0:
            return False
        target = total // 4 

        self.reverse_flag = True  
        if matchsticks[0] >= target//2:
            self.reverse_flag = False        

        self.dfs(target, total, matchsticks, 0, [0, 0, 0, 0]) 
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
