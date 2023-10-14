from typing import * 

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        def bsearch_smaller(dry_days, target): 
            # find the last sunny day < target 
            l, r = 0, len(dry_days)-1
            while l <= r: 
                mid = (r-l)//2+l 
                if dry_days[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1  
            return r
         
        def bsearch_larger(dry_days, target): 
            # find the first sunny day > target 
            l, r = 0, len(dry_days)-1
            while l <= r: 
                mid = (r-l)//2+l 
                if dry_days[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1  
            return l 
        
        n = len(rains)
        dry_days = []
        rain_days = {}
        ans = [-1]*n 
        
        for i in range(n): 
            if rains[i] == 0: 
                dry_days.append(i)
                continue 
            if rain_days.get(rains[i], -1) == -1:
                rain_days[rains[i]] = i 
                continue 
            
            # city is already flooded, find first sunny day to dry it
            sunny1 = bsearch_larger(dry_days, rain_days[rains[i]])
            sunny2 = bsearch_smaller(dry_days, i)
            if sunny1 < 0 or sunny2 >= len(dry_days) or sunny2 < sunny1: 
                return []
            sunny = dry_days[sunny1]
            dry_days.remove(sunny)
            ans[sunny] = rains[i]
            # update last rain day for this city 
            rain_days[rains[i]] = i
        
        # must dry a lake on dry days 
        for d in dry_days: 
            ans[d] = 1
    
        return ans 

if __name__ == "__main__": 
    s = Solution()
    
    # assert s.avoidFlood([69,0,0,0,69]) == [-1,69,1,1,-1]
    assert s.avoidFlood([1,2,0,0,2,1]) == [-1,-1,2,1,-1,-1]