from typing import * 

# TLE
class Solution:
    def backtracking(self, total, used_match_num, remain, matchsticks, start_idx, sides): 
        # base case 
        if self.success: 
            return 
        if start_idx == len(matchsticks):
            if used_match_num != len(matchsticks):
                return 
            if sides[0] == sides[1] == sides[2] == sides[3]:
                self.success = True 
            return 
        
        for i in range(start_idx, len(matchsticks)):
            for j in range(len(sides)):
                # prune 
                if sides[j] + remain < total / 4: 
                    return 
                if sides[j] > total / 4: 
                    return 
                if sides[j] + matchsticks[i] > total / 4: 
                    continue 
                remain -= matchsticks[i] 
                sides[j] += matchsticks[i]
                used_match_num += 1 
                self.backtracking(total, used_match_num, remain, matchsticks, i+1, sides)
                sides[j] -= matchsticks[i]
                used_match_num -= 1 
                remain += matchsticks[i] 
        
    def makesquare(self, matchsticks: List[int]) -> bool:
        self.success = False 
        total = sum(matchsticks) 
        if total % 4 != 0:
            return False
        self.backtracking(total, 0, total, matchsticks, 0, [0, 0, 0, 0]) 
        return self.success 

if __name__ == "__main__": 
    s = Solution() 

    matchsticks = [1,1,2,2,2]
    assert s.makesquare(matchsticks) 

    matchsticks = [3,3,3,3,4]
    assert not s.makesquare(matchsticks) 

    matchsticks = [2,2,2,2,2,2]
    assert not s.makesquare(matchsticks) 