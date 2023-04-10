from typing import * 

class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        hashmap = {}
        for i, l in enumerate(s): 
            cur = hashmap.get(l, [])
            cur.append(i)
            hashmap[l] = cur
        for k, v in hashmap.items(): 
            if v[1]-v[0]-1 != distance[ord(k)-ord("a")]:
                return False 
        return True 
  
if __name__ == "__main__": 
    sol = Solution() 
    
    s = "aa"
    distance = [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    assert not sol.checkDistances(s, distance)  