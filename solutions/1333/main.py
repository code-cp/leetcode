from typing import * 

class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        res = []
        for r in restaurants: 
            if veganFriendly == 1 and r[2] == 0: 
                continue 
            if r[3] > maxPrice: 
                continue 
            if r[4] > maxDistance: 
                continue 
            res.append(r)
        res.sort(key=lambda x: (x[1], x[0]), reverse=True)
        return [r[0] for r in res] 
                