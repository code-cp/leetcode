from typing import * 
import heapq 

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # sort trip by from 
        trips.sort(key=lambda x: x[1])
        people = []
        cur_num = 0 
        
        for (p, f, t) in trips: 
            # pop out people who reach destination 
            # NOTE, <= f, not < f 
            while len(people) > 0 and people[0][0] <= f: 
                (_, leave) = heapq.heappop(people) 
                cur_num -= leave 
            cur_num += p 
            if cur_num > capacity: 
                return False
            heapq.heappush(people, (t, p))
            
        return True 
    
if __name__ == "__main__": 
    s = Solution()
    
    assert s.carPooling([[2,1,5],[3,5,7]], 3) 
    # assert s.carPooling([[2,1,5],[3,3,7]], 5)  
    # assert not s.carPooling([[2,1,5],[3,3,7]], 4) 
            
                