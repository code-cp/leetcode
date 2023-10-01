from typing import * 

class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        # sort based on which flower will bloom earliest 
        n = len(plantTime)
        bloom_time = [[] for _ in range(n)]
        for i in range(n): 
            # given a deadline T for all flowers, 
            # always need to tackle the earliest T-growTime[i] first 
            bloom_time[i].append((plantTime[i], growTime[i]))
        # NOTE, not x: x[1]
        bloom_time.sort(key=lambda x: x[0][1], reverse=True)
        
        def isValid(deadline):
            nonlocal n 
            nonlocal bloom_time
            
            days = 0 
            for i in range(n): 
                plant, grow = bloom_time[i][0]
                days += plant
                # must plant flower i before deadline - grow  
                if days > deadline - grow:
                    return False 
                
            return True 
        
        l, r = 1, sum(plantTime) + sum(growTime)
        while l <= r: 
            mid = (r-l)//2+l 
            if isValid(mid):
                r = mid-1 
            else: 
                l = mid+1 
                
        return l 

if __name__ == "__main__": 
    s = Solution()
    
    assert s.earliestFullBloom([1,4,3], [2,3,1]) == 9
        