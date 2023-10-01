from typing import * 
from collections import defaultdict
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        flowers_map = defaultdict(int)
        for f in flowers: 
            start, end = f[0], f[1]
            flowers_map[start] += 1 
            flowers_map[end+1] -= 1
        
        # time, diff 
        diff = []
        for k, v in flowers_map.items(): 
            diff.append((k, v))
        diff.sort()
        
        # time, index 
        people_sorted = []
        for i in range(len(people)): 
            people_sorted.append((people[i], i))
        people_sorted.sort()
        
        ans = [0]*len(people)
        total = 0 
        j = 0 
        for i in range(len(people)): 
            while j < len(diff) and diff[j][0] <= people_sorted[i][0]: 
                # accumulate the number in diff 
                total += diff[j][1]
                j += 1 
            ans[people_sorted[i][1]] = total
        
        return ans 
            
            