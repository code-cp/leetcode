from typing import * 
from collections import defaultdict 
class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        def move(cur, facing, c): 
            new_x, new_y = cur[0], cur[1]
            if c == -2: 
                facing = (facing - 1) % 4 
                return (new_x, new_y), facing 
        
            if c == -1: 
                facing = (facing + 1) % 4 
                return (new_x, new_y), facing 
            
            if facing == 0: 
                new_y += c
            elif facing == 1:
                new_x += c
            elif facing == 2:
                new_y -= c
            else: 
                new_x -= c
            return (new_x, new_y), facing 
        
        def checkMove(cur, nex, facing, obs_x, obs_y): 
            new_x, new_y = nex[0], nex[1]
            if facing == 0: 
                obs = obs_x[cur[0]]
                for y in obs: 
                    if y > cur[1] and y <= nex[1]: 
                        new_y = y-1 
                        return (new_x, new_y) 
            if facing == 1: 
                obs = obs_y[cur[1]]
                for x in obs: 
                    if x > cur[0] and x <= nex[0]: 
                        new_x = x-1 
                        return (new_x, new_y) 
            if facing == 2: 
                obs = obs_x[cur[0]]
                for y in obs: 
                    if y < cur[1] and y >= nex[1]: 
                        new_y = y+1 
                        return (new_x, new_y) 
            if facing == 3: 
                obs = obs_y[cur[1]]
                for x in obs: 
                    if x < cur[0] and x >= nex[0]: 
                        new_x = x+1 
                        return (new_x, new_y) 
            return (new_x, new_y)  
        
        obs_x = defaultdict(list)
        obs_y = defaultdict(list)
        for ob in obstacles: 
            obs_x[ob[0]].append(ob[1])
            obs_y[ob[1]].append(ob[0])
        
        cur = (0,0)
        facing = 0 
        res = 0 
        for c in commands: 
            nex, facing = move(cur, facing, c)
            nex = checkMove(cur, nex, facing, obs_x, obs_y)
            cur = nex 
            res = max(res, cur[0]**2 + cur[1]**2)
            
        return res 

if __name__ == "__main__": 
    s = Solution()
    
    # assert s.robotSim([4,-1,4,-2,4], [[2,4]]) == 65 
    assert s.robotSim([6,-1,-1,6], []) == 36 