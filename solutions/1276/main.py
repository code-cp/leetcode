from typing import * 

class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        ans = []
        if tomatoSlices % 2 == 1: 
            return ans
        # 4X + 2Y = tomato
        # X + Y = cheese
        # X = (4*cheese-tomato)/2 
        # Y = tomato-cheese-3*X 
        y = (4*cheeseSlices - tomatoSlices) // 2 
        if y < 0: 
            return ans 
        if (tomatoSlices - cheeseSlices - y) % 3 != 0: 
            return ans 
        x = (tomatoSlices - cheeseSlices - y) // 3  
        if x < 0: 
            return ans 
        ans = [x, y]
        return ans 