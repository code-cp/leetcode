from typing import * 
from collections import defaultdict
class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        n = len(values)
        indice = sorted(range(n), key=lambda i: values[i], reverse=True) 
        values = [values[i] for i in indice] 
        labels = [labels[i] for i in indice]
        used = defaultdict(int)
        ans = 0
        cnt = 0 
        for v, l in zip(values, labels):
            if cnt == numWanted: 
                break  
            if used[l] < useLimit: 
                used[l] += 1 
                ans += v 
                cnt += 1 
        return ans 
         
if __name__ == "__main__": 
    s = Solution() 
    
    values = [5,4,3,2,1]
    labels = [1,3,3,3,2]
    numWanted = 3
    useLimit = 2
    assert s.largestValsFromLabels(values, labels, numWanted, useLimit) == 12 