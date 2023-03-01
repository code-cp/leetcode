from typing import * 

class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        ret = []
        items1.sort(key=lambda x: x[0])
        items2.sort(key=lambda x: x[0])
        m, n = len(items1), len(items2)

        i = j = 0 
        while i < m and j < n: 
            if items1[i][0] == items2[j][0]:
                ret.append([items1[i][0], items1[i][1]+items2[j][1]])
                i += 1 
                j += 1 
            elif items1[i][0] < items2[j][0]:
                ret.append(items1[i]) 
                i += 1 
            else: 
                ret.append(items2[j])
                j += 1 

        while i < m: 
            ret.append(items1[i])
            i += 1 
        
        while j < n: 
            ret.append(items2[j])
            j += 1 

        return ret 
