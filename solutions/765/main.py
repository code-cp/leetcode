from typing import * 

class Solution:    
    def minSwapsCouples(self, row: List[int]) -> int:
        def findFather(father, x): 
            if father[x] != x: 
                father[x] = findFather(father, father[x])
            return father[x]
        
        def Union(father, x, y): 
            x = father[x]
            y = father[y]
            if (x < y): 
                father[y] = x 
            else: 
                father[x] = y 
        
        n = len(row)
        father = [0]*n 
        
        for i in range(0, n, 2):
            # put a couple in the same group  
            father[i] = i
            father[i+1] = i
            
        for i in range(0, n, 2):
            # put adjacent people in same group  
            a, b = row[i], row[i+1]
            if findFather(father, a) != findFather(father, b): 
                Union(father, a, b)  
                
        # key = father, value = group size 
        groups = {}
        for i in range(n): 
            groups[findFather(father, i)] = groups.get(findFather(father, i), 0) + 1  
            
        res = 0 
        for k, v in groups.items(): 
            res += v//2 - 1 
            
        return res 
        
if __name__ == "__main__": 
    s = Solution()
    
    assert s.minSwapsCouples([0,2,1,3]) == 1